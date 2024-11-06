from django.shortcuts import get_object_or_404
from rest_framework import generics

from apps.products.models import Product
from rest_framework.permissions import IsAdminUser
from .models import ProductIMG
from .serializers import ProductIMGSerializer


class ProductIMGListView(generics.CreateAPIView):
    queryset = ProductIMG.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ProductIMGSerializer


class ProductimegesListView(generics.ListAPIView):
    serializer_class = ProductIMGSerializer

    def get_queryset(self):
        product_slug = self.kwargs["product_slug"]
        product = get_object_or_404(Product, slug=product_slug)
        return ProductIMG.objects.filter(product_id=product)
