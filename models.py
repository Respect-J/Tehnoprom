import uuid
from enum import Enum

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PaymentProvider(models.IntegerChoices):
    UNKNOWN = 0
    PAYME = 1
    UZUM_PAY = 2
    UZUM_NASIYA = 3
