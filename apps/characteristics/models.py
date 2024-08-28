from django.db import models
from models import BaseModel
from apps.products.models import Product


class Characteric(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='characteristics',
                                verbose_name="выберите товар")

    def __str__(self):
        return f"характеристики для товара {self.product}"

    class Meta:
        verbose_name = "характеристики"
        verbose_name_plural = "характеристики"


class CharacteristicItem(models.Model):
    characteristic = models.ForeignKey(Characteric, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=512, null=True, blank=True, verbose_name="Название характеристики")
    value = models.CharField(max_length=512, null=True, blank=True, verbose_name="Значение характеристики")

    def __str__(self):
        return f"{self.name}: {self.value}"

    class Meta:
        verbose_name = "характеристики"
        verbose_name_plural = "характеристики"
