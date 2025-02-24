from django.urls import path
from pyclick.views import ClickMerchantServiceView, CreateClickTransactionView

from apps.payment.click.views import ClickTransactionTestView  # Use custom handler

urlpatterns = [
    path("transaction/create/", CreateClickTransactionView.as_view()),
    path("transaction/", ClickTransactionTestView.as_view()),
    path("service/<service_type>", ClickMerchantServiceView.as_view()),
]
