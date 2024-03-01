from django.shortcuts import get_object_or_404
from rest_framework import generics

from apps.products.models import Product

from .models import ProductIMG
from .serializers import ProductIMGSerializer


class ProductIMGListView(generics.CreateAPIView):
    queryset = ProductIMG.objects.all()
    serializer_class = ProductIMGSerializer


class ProductimegesListView(generics.ListAPIView):
    serializer_class = ProductIMGSerializer

    def get_queryset(self):
        product_id = self.kwargs["product_id"]
        return ProductIMG.objects.filter(category_id=product_id)
