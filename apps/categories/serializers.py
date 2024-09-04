from rest_framework import serializers

from .models import Category, PopularCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PopularCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(source='categorys', many=True)

    class Meta:
        model = PopularCategory
        fields = ['id', 'category']
