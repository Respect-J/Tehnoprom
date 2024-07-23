from rest_framework import generics
from .models import Banner
from .serializers import BannersSerializer


class BannersListView(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannersSerializer

