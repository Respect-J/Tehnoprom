from rest_framework import generics
from apps.collections.models import Collection
from .models import Category, PopularCategory
from apps.brands.models import BrandForCategory
from django.shortcuts import get_object_or_404
from .serializers import CategorySerializer, PopularCategorySerializer
from rest_framework.response import Response


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoriesByCollectionUUID(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        collection_id = self.kwargs["collection_id"]
        collection = get_object_or_404(Collection, id=collection_id)
        return Category.objects.filter(collection=collection)


class CollectionCategoryBrandView(generics.ListAPIView):

    def get(self, request, *args, **kwargs):

        try:
            uuid = kwargs.get('collection_id', None)
            collection = Collection.objects.get(id=uuid)
        except Collection.DoesNotExist:
            raise Http404


        categories = Category.objects.filter(collection=collection)


        result = []
        for category in categories:

            brands = BrandForCategory.objects.filter(category_id=category)
            brands_data = [{'brand_id': brand.id, 'brand_title': brand.title} for brand in brands]


            result.append({
                'category_id': category.id,
                'category_title': category.title,
                'children': brands_data
            })

        return Response(result)


class PopularCategoryListView(generics.ListAPIView):
    queryset = PopularCategory.objects.all()
    serializer_class = PopularCategorySerializer
