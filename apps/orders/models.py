from django.db import models

from apps.users.models import UserModel
from models import BaseModel, PaymentProvider


class Order(BaseModel):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    delivery_address = models.CharField(max_length=255, blank=True)
    payment_provider = models.IntegerField(choices=PaymentProvider, default=PaymentProvider.UNKNOWN)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
