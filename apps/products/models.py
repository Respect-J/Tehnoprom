from django.db import models

from apps.brands.models import Brand
from apps.categories.models import Category
from models import BaseModel


class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория товара")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Бренд товара")
    title = models.CharField(max_length=256, null=True, blank=True, verbose_name="Название товара")
    description = models.TextField(null=True, blank=True, verbose_name="Описание товара")
    mainimg = models.ImageField(upload_to="img/products/", null=True, blank=True, verbose_name="Главная картинка")
    stock_quantity = models.PositiveIntegerField(null=True, blank=True, default=0,
                                                 verbose_name="Количество товара (не обязательно для заполнения)")
    # payment parameters
    package_code = models.CharField(max_length=256, null=True, blank=True, verbose_name="Код упаковки товара")
    code = models.CharField(max_length=256, null=True, blank=True, verbose_name="Код товара")
    price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True, verbose_name="Цена товара")
    priceusd = models.CharField(max_length=100, null=True, blank=True, default=0, verbose_name="Цена в долларах")
    vat_percent = models.DecimalField(max_digits=100, decimal_places=0, null=True, blank=True, verbose_name="НДС")

    def __str__(self):
        return self.title

    def get_main_image_url(self):
        return self.mainimg.url if self.mainimg else None

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
