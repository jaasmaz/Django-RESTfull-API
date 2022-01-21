from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import Collection, OrderItem, Product
from .serializers import ProductSerializer, CollectionSerializer

# Generic API View Class
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

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
