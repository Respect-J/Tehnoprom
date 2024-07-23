from rest_framework import serializers

from .models import BrandForCategory, Brands


class BrandCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandForCategory
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = "__all__"
