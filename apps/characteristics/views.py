from rest_framework import generics
from .models import Characteric
from django.shortcuts import get_object_or_404
from .serializers import CharacteristicItemSerializer
from apps.products.models import Product


class CharactericView(generics.ListAPIView):
    serializer_class = CharacteristicItemSerializer

    def get_queryset(self):
        product_slug = self.kwargs["product_slug"]
        product = get_object_or_404(Product, slug=product_slug)
        return Characteric.objects.filter(product=product)
