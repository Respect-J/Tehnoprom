from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

from apps.brands.models import Brand
from apps.categories.models import Category

from .models import Product
from .serializers import ProductSerializer


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BrandProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        brand_id = self.kwargs["brand_id"]
        brand = get_object_or_404(Brand, id=brand_id)
        return Product.objects.filter(brand=brand)


class CategoryProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs["category_id"]
        category = get_object_or_404(Category, id=category_id)
        return Product.objects.filter(category=category)
