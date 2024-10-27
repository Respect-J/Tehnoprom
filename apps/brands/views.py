from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import BrandForCategory, Brands
from apps.categories.models import Category
from .serializers import BrandCategorySerializer, BrandSerializer


class BrandListView(generics.ListAPIView):
    queryset = BrandForCategory.objects.all()
    serializer_class = BrandCategorySerializer


class BrandsByCategorySlug(generics.ListAPIView):
    serializer_class = BrandCategorySerializer

    def get_queryset(self):
        category_slug = self.kwargs["category_slug"]
        category = get_object_or_404(Category, slug=category_slug)
        return BrandForCategory.objects.filter(category_id=category)


class BrandView(generics.ListAPIView):
    queryset = Brands.objects.all()
    serializer_class = BrandSerializer
