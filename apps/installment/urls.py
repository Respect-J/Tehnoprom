from django.urls import path
from .views import CalculateInstallmentView

urlpatterns = [
    path('api/calculate_installment/', CalculateInstallmentView.as_view(), name='calculate_installment'),
]