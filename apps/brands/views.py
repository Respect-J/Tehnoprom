from rest_framework import generics
from .models import Brand
from .serializers import BrandSerializer


class BrandListView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

# Create your views here.
