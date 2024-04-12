from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Banner
from .serializers import BannersSerializer


class BannersListView(generics.ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannersSerializer

    def get_permissions(self):

        if self.request.method == "POST":
            return [IsAdminUser()]
        return [AllowAny()]


class BannersRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Banner.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = BannersSerializer
