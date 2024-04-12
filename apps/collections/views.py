from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Collection
from .serializers import CollectionSerializer


class CollectionListView(generics.ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminUser()]
        return [AllowAny()]


class CollectionRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = CollectionSerializer
