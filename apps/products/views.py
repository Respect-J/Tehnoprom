from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from apps.brands.models import BrandForCategory, Brands
from apps.categories.models import Category
from .models import Product, PopularProduct, DayProduct
from .serializers import ProductSerializer, PopularProductSerializer, DayProductSerializer
from rest_framework.permissions import IsAdminUser, AllowAny


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination


class ProductRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminUser()]


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


class PopularProductListView(generics.ListAPIView):
    queryset = PopularProduct.objects.all()
    serializer_class = PopularProductSerializer
    pagination_class = StandardResultsSetPagination


class DayProductListView(generics.ListAPIView):
    queryset = DayProduct.objects.all()
    serializer_class = DayProductSerializer
