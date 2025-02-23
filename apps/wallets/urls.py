from django.urls import path
from .views import UserWalletView

urlpatterns = [
    path('my-wallet/', UserWalletView.as_view(), name='my_wallet'),
]