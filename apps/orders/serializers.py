from rest_framework import serializers

from .models import Order


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["user", "amount", "delivery_address", "payment_provider"]
