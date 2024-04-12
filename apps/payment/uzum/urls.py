from django.urls import path

from .views import CalculateTariffsView, CheckStatusView, ConfirmContractView, CreateOrderView

urlpatterns = [
    path("nasiya/check-status", CheckStatusView.as_view(), name="Nasiya Check Status"),
    path("nasiya/calculate-tariffs", CalculateTariffsView.as_view(), name="Nasiya Calculate tariffs"),
    path("nasiya/create-order", CreateOrderView.as_view(), name="Nasiya Create order"),
    path("nasiya/confirm-contract", ConfirmContractView.as_view(), name="Nasiya Confirm contract"),
]
