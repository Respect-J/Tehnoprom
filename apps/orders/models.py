from django.db import models

from apps.products.models import Product
from apps.users.models import UserModel
from models import BaseModel


class Order(BaseModel):
    STATUS_CHOICES = [
        (1, 'Заказ принят'),
        (2, 'Заказ одобрен'),
        (3, 'Заказ в пути'),
        (4, 'Заказ доставлен'),
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    phone_number = models.CharField(max_length=13, blank=True)
    amount = models.IntegerField(default=0)
    delivery_address = models.CharField(max_length=255, blank=True)
    is_paid = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    def calculate_total_amount(self):
        # Логика вычисления общей суммы заказа на основе продуктов
        total = sum(product.price for product in self.products.all())
        return total

    def __str__(self):
        return str(self.id)
