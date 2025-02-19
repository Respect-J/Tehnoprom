import random

from django.db import models

from apps.products.models import Product
from apps.users.models import UserModel
from models import BaseModel


class Order(BaseModel):
    # Переопределяем id на CharField длиной 6
    id = models.CharField(max_length=6, primary_key=True, editable=False, unique=True)

    STATUS_CHOICES = [
        (1, "Заказ принят"),
        (2, "Заказ одобрен"),
        (3, "Заказ в пути"),
        (4, "Заказ доставлен"),
    ]

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name="Клиент")
    phone_number = models.CharField(max_length=13, blank=True, verbose_name="Номер заказчика")
    delivery_address = models.CharField(max_length=255, blank=True, verbose_name="Адрес доставки")
    is_paid = models.BooleanField(default=False, verbose_name="Статус оплаты")
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name="Статус заказа")
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Общая сумма заказа")
    temp = models.CharField(max_length=13, blank=True)

    def calculate_total_amount(self):
        """Пересчитывает сумму заказа"""
        total = sum(item.quantity * item.price_at_order_time for item in self.order_items.all())
        return total

    def generate_unique_id(self):
        """Генерирует уникальный 6-значный код."""
        while True:
            # генерируем случайное число от 100000 до 999999
            random_code = str(random.randint(100000, 999999))
            # проверяем, нет ли уже заказа с таким ID
            if not Order.objects.filter(id=random_code).exists():
                return random_code

    def save(self, *args, **kwargs):
        """Перед сохранением:
        - если id ещё не задан, генерируем случайный 6-значный.
        - пересчитываем сумму заказа.
        """
        if not self.id:
            self.id = self.generate_unique_id()
        self.amount = self.calculate_total_amount()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Заказ #{self.id} от {self.user}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="order_items", on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    price_at_order_time = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена на момент заказа")

    def __str__(self):
        return f"{self.product.title} x{self.quantity} (Заказ #{self.order.id})"

    class Meta:
        verbose_name = "Позиция заказа"
        verbose_name_plural = "Позиции заказа"
