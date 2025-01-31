from django.urls import path

from .views import CreateOrderView, UserOrdersView

urlpatterns = [
    path("", CreateOrderView.as_view(), name="create-order"),
    path("my-orders/", UserOrdersView.as_view(), name='user-orders'),
]
