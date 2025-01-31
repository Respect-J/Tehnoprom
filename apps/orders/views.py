from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CreateOrderSerializer, OrderSerializer
from .models import Order
from apps.users.models import UserModel


class CreateOrderView(CreateAPIView):

    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CreateOrderSerializer

    def perform_create(self, serializer):
        """Привязываем заказ к текущему пользователю (UserModel)"""
        user = UserModel.objects.get(id=self.request.user.id)
        serializer.save(user=user)


class UserOrdersView(ListAPIView):

    serializer_class = OrderSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
