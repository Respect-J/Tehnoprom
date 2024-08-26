from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CreateOrderSerializer, OrderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order


class CreateOrderView(CreateAPIView):
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CreateOrderSerializer


class UserOrdersView(APIView):
    def get(self, request, user_id, format=None):
        orders = Order.objects.filter(user_id=user_id)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
