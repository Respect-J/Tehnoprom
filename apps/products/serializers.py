from rest_framework import serializers
from .models import Product, PopularProduct

class ProductSerializer(serializers.ModelSerializer):
    discounted_price = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = "__all__"


class PopularProductSerializer(serializers.ModelSerializer):
    products = ProductSerializer(source='product', many=True)

    class Meta:
        model = PopularProduct
        fields = ['id', 'products']