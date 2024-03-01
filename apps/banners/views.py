from rest_framework import generics

from .models import Banner
from .serializers import BannersSerializer


class BannersListView(generics.ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannersSerializer


class BannersRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannersSerializer
