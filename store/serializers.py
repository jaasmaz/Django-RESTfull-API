#Serializers used to convert an object to python dictionary
from rest_framework import serializers
from store.models import Collection, Product
from decimal import Decimal

class CollectionSerializer(serializers.Serializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'price_with_tax', 'collection', 'updated_on']

    updated_on = serializers.DateTimeField(source='last_update')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        return product.price * Decimal(1.1)