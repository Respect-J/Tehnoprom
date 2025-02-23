from django.db import models
from models import BaseModel
from apps.users.models import UserModel


class Wallet(BaseModel):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name='wallet',
        verbose_name='Пользователь'
    )
    balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name='Баланс'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    def __str__(self):
        return f"Кошелек пользователя {self.user.username} (Баланс: {self.balance})"


class Transaction(BaseModel):

    DEPOSIT = 'deposit'
    WITHDRAW = 'withdraw'
    TRANSACTION_TYPES = [
        (DEPOSIT, 'Пополнение'),
        (WITHDRAW, 'Снятие'),
    ]

    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.CASCADE,
        related_name='transactions',
        verbose_name='Кошелек'
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Сумма'
    )
    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPES,
        verbose_name='Тип транзакции'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание транзакции'
    )

    def __str__(self):
        return f"{self.get_transaction_type_display()} - {self.amount} (Кошелек ID: {self.wallet.id})"
