#Serializers used to convert an object to python dictionary
from dataclasses import fields
from xml.parsers.expat import model
from rest_framework import serializers
from store.models import Collection, Product, Review
from decimal import Decimal

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description','slug', 'inventory','price', 'price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        return product.price * Decimal(1.1)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date', 'name', 'description', 'product']