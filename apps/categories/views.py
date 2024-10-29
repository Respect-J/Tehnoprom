from rest_framework import generics
from apps.collections.models import Collection
from .models import Category, PopularCategory
from apps.brands.models import BrandForCategory
from django.shortcuts import get_object_or_404
from .serializers import CategorySerializer, PopularCategorySerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoriesByCollectionSlug(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        collection_slug = self.kwargs["collection_slug"]
        collection = get_object_or_404(Collection, slug=collection_slug)
        return Category.objects.filter(collection=collection)


class CollectionCategoryBrandView(APIView):
    def get(self, request, *args, **kwargs):
        collection_slug = self.kwargs["collection_slug"]
        collection = get_object_or_404(Collection, slug=collection_slug)

        categories = Category.objects.filter(collection=collection)

        result = []
        for category in categories:
            brands = BrandForCategory.objects.filter(category_id=category)
            brands_data = [{'brand_slug': brand.slug, 'brand_title': brand.title} for brand in brands]

            result.append({
                'category_slug': category.slug,
                'category_title': category.title,
                'children': brands_data
            })

        return Response(result)


class PopularCategoryListView(generics.ListAPIView):
    queryset = PopularCategory.objects.all()
    serializer_class = PopularCategorySerializer
