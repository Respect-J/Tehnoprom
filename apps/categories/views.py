from rest_framework import generics
from apps.collections.models import Collection
from .models import Category
from django.shortcuts import get_object_or_404
from .serializers import CategorySerializer


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoriesByCollectionUUID(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        collection_id = self.kwargs["collection_id"]
        collection = get_object_or_404(Collection, id=collection_id)
        return Category.objects.filter(collection=collection)


