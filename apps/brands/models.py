from django.db import models
from apps.categories.models import Category
from models import BaseModel


class BrandForCategory(BaseModel):
    title = models.CharField(max_length=256, null=True, blank=True, verbose_name="Название на русском")
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="категория")
    logo = models.ImageField(upload_to="img/brands/", null=True, blank=True, verbose_name="Логотип")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Бренд для категории"
        verbose_name_plural = "Бренд для категории"


class Brands(BaseModel):
    title = models.CharField(max_length=256, null=True, blank=True, verbose_name="Название на русском")
    logo = models.ImageField(upload_to="img/brands/", null=True, blank=True, verbose_name="Логотип")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренд"
