from rest_framework import generics
from .models import Characteric
from django.shortcuts import get_object_or_404
from .serializers import CharactericSerializer
from apps.products.models import Product


class CharactericVIEW(generics.ListAPIView):
    serializer_class = CharactericSerializer

    def get_queryset(self):
        product_id = self.kwargs["product_id"]
        a = get_object_or_404(Product, id=product_id)
        return Characteric.objects.filter(product_id=a)
