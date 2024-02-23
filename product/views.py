from rest_framework import generics
from .models import Product
from brand.models import Brand
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BrandProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        brand_id = self.kwargs['brand_id']
        brand = get_object_or_404(Brand, id=brand_id)
        return Product.objects.filter(brand=brand)
