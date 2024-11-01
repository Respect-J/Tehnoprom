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

    id = models.AutoField(primary_key=True, verbose_name="id заказа")
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name="имя клиента")
    products = models.ManyToManyField(Product, verbose_name="список товаров")
    phone_number = models.CharField(max_length=13, blank=True, verbose_name="популярные товары")
    amount = models.IntegerField(default=0, verbose_name="количество")
    delivery_address = models.CharField(max_length=255, blank=True, verbose_name="адресс доставки")
    is_paid = models.BooleanField(default=False, verbose_name="статус оплаты")
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name="статус заказа")

    def calculate_total_amount(self):
        # Логика вычисления общей суммы заказа на основе продуктов
        total = sum(product.price for product in self.products.all())
        return total

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
