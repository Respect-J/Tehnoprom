from django.db import models
from models import BaseModel
from apps.products.models import Product


class Characteric(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='characteristics')

    def __str__(self):
        return f"Characteristics for {self.product}"


class CharacteristicItem(models.Model):
    characteristic = models.ForeignKey(Characteric, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=512, null=True, blank=True)
    value = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return f"{self.name}: {self.value}"
