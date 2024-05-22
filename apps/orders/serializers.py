from rest_framework import serializers

from .models import Order


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "user", "amount", "delivery_address", 'phone_number', 'products']