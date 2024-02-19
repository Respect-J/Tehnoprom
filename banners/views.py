from rest_framework import generics
from .models import Banners
from .serializers import BannersSerializer


class BannersListView(generics.ListCreateAPIView):
    queryset = Banners.objects.all()
    serializer_class = BannersSerializer


class BannersRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Banners.objects.all()
    serializer_class = BannersSerializer
