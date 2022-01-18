#Serializers used to convert an object to python dictionary
from rest_framework import serializers
from store.models import Collection, Product
from decimal import Decimal

class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    collection = serializers.HyperlinkedRelatedField(
        queryset = Collection.objects.all(),
        view_name= 'collection-detail',
    )
    updated_on = serializers.DateTimeField(source='last_update')

    def calculate_tax(self, product: Product):
        return product.price * Decimal(1.1)