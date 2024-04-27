from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import Brand
from apps.categories.models import Category
from .serializers import BrandSerializer
from rest_framework.permissions import IsAdminUser, AllowAny


class BrandListView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def get_permissions(self):

        if self.request.method == "POST":
            return [IsAdminUser()]
        return [AllowAny()]



class BrandRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = BrandSerializer


class BrandsByCategoriUUID(generics.ListAPIView):
    serializer_class = BrandSerializer

    def get_queryset(self):
        category_id = self.kwargs["category_id"]
        category = get_object_or_404(Category, id=category_id)
        return Brand.objects.filter(category_id=category)
# Create your views here.
