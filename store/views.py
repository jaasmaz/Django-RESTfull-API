from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from .pagination import DefaultPagination
from .models import Collection, OrderItem, Product, Review
from .serializers import ProductSerializer, CollectionSerializer, ReviewSerializer
from .filters import ProductFilter

# Generic API View Class
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['inventory']
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    search_fields = ['title','description']
    ordering_fields = ['price', 'last_update']

    def get_serializer_context(self):
        return {'request': self.request}

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Product Cannot be deleted its associated with order item'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request,*args,**kwargs)

class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(product_count = Count('products')).all()
    serializer_class = CollectionSerializer

    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id=kwargs['pk']).count() > 0:
            return Response({'error': 'collection Cannot be deleted its associated with a product'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request,*args,**kwargs)

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk'],}