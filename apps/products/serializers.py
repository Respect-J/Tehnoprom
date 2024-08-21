from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    discounted_price = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = "__all__"
