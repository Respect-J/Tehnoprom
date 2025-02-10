from django.db import models
from django.utils import timezone
from apps.users.models import UserModel


class PremiumPlan(models.Model):

    name = models.CharField(max_length=100, unique=True)
    duration_in_days = models.PositiveIntegerField(help_text="Срок действия тарифа в днях")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Стоимость тарифа")
    discount_percentage = models.PositiveIntegerField(help_text="Процент скидки", default=0)
    discount_limit = models.DecimalField(max_digits=15, decimal_places=2, default=0,
                                         help_text="Максимальная сумма заказа для скидки")

    def __str__(self):
        return f"{self.name} ({self.duration_in_days} дней)"


class UserPremiumSubscription(models.Model):

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE,  related_name='subscriptions')
    plan = models.ForeignKey(
        PremiumPlan,
        on_delete=models.CASCADE,
        related_name='subscriptions'
    )
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Подписка {self.user} на {self.plan.name}"
