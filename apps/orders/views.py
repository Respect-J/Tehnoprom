from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser

from .models import Order
from .serializers import CreateOrderSerializer


class CreateOrderView(CreateAPIView):
    queryset = Order.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = CreateOrderSerializer
