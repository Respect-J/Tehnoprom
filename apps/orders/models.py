from django.db import models

from apps.products.models import Product
from apps.users.models import UserModel
from models import BaseModel


class Order(BaseModel):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    phone_number = models.CharField(max_length=13, blank=True)
    amount = models.IntegerField(default=0)
    delivery_address = models.CharField(max_length=255, blank=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
