from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from apps.brands.models import BrandForCategory, Brands
from apps.categories.models import Category
from .models import Product, PopularProduct, DayProduct
from .serializers import ProductSerializer, PopularProductSerializer, DayProductSerializer
from rest_framework.response import Response

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination


class ProductDetailBySlugView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'


class BrandCategoryProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        brand_slug = self.kwargs["brand_slug"]
        brand = get_object_or_404(BrandForCategory, slug=brand_slug)
        return Product.objects.filter(brandcategory_id=brand)


class CategoryProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        category_slug = self.kwargs["category_slug"]
        category = get_object_or_404(Category, slug=category_slug)
        return Product.objects.filter(category=category)


class BrandProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        brand_slug = self.kwargs["brand_slug"]
        brand = get_object_or_404(Brands, slug=brand_slug)
        return Product.objects.filter(brands=brand)


class PopularProductListView(generics.GenericAPIView):
    serializer_class = PopularProductSerializer
    queryset = PopularProduct.objects.all()

    def get(self, request, *args, **kwargs):
        popular_product = PopularProduct.objects.first()
        if not popular_product:
            return Response({"detail": "Нет популярных товаров"}, status=404)

        serializer = self.get_serializer(popular_product)
        return Response(serializer.data)


class DayProductListView(generics.ListAPIView):
    queryset = DayProduct.objects.all()
    serializer_class = DayProductSerializer

