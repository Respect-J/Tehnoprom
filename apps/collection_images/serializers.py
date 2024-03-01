from rest_framework import serializers
from .models import ProductIMG


class ProductIMGSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductIMG
        fields = "__all__"

