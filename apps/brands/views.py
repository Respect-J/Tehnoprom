from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import BrandForCategory, Brands
from apps.categories.models import Category
from .serializers import BrandCategorySerializer, BrandSerializer


class BrandListView(generics.ListAPIView):
    queryset = BrandForCategory.objects.all()
    serializer_class = BrandCategorySerializer


class BrandsByCategoriUUID(generics.ListAPIView):
    serializer_class = BrandCategorySerializer

    def get_queryset(self):
        category_id = self.kwargs["category_id"]
        category = get_object_or_404(Category, id=category_id)
        return BrandForCategory.objects.filter(category_id=category)


class BrandView(generics.ListAPIView):
    queryset = Brands.objects.all()
    serializer_class = BrandSerializer
