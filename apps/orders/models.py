from django.db import models

from apps.users.models import UserModel
from models import BaseModel, PaymentProvider


class Order(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=255, blank=True)
    payment_provider = models.IntegerField(choices=PaymentProvider, default=PaymentProvider.UNKNOWN)
    is_paid = models.BooleanField(default=False)
