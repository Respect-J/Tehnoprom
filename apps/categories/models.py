from django.db import models

from apps.collections.models import Collection
from models import BaseModel


class Category(BaseModel):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, verbose_name="Коллекция")
    title = models.CharField(max_length=256, null=True, blank=True, verbose_name="Название")
    img = models.ImageField(upload_to="img/categories/", null=True, blank=True, verbose_name="Картинка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
