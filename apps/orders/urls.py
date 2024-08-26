from django.urls import path

from .views import CreateOrderView, UserOrdersView

urlpatterns = [
    path("", CreateOrderView.as_view(), name="create-order"),
    path('<int:user_id>', UserOrdersView.as_view(), name='user-orders'),
]
