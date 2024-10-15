from django.db import models

from apps.collections.models import Collection
from models import BaseModel


class Category(BaseModel):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, verbose_name="Коллекция")
    title = models.CharField(max_length=256, null=True, blank=True, verbose_name="Название")
    img = models.ImageField(upload_to="img/categories/", null=True, blank=True, verbose_name="Картинка")
    seo_key = models.CharField(max_length=60, null=True, blank=True, verbose_name="Ключ слово для СЕО")
    title_key = models.CharField(max_length=60, null=True, blank=True, verbose_name="Title слово для СЕО")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class PopularCategory(BaseModel):
    categorys = models.ManyToManyField(Category, verbose_name="популярные категории")

    def __str__(self):
        return f"Группа популярных категория"

    class Meta:
        verbose_name = "Популярные категории"
        verbose_name_plural = "Популярные категории"
