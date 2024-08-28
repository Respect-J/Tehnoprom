from django.db import models
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from apps.brands.models import BrandForCategory, Brands
from apps.categories.models import Category
from models import BaseModel


class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория товара")
    brandcategory = models.ForeignKey(BrandForCategory, on_delete=models.CASCADE, verbose_name="Бренд категории товара")
    brands = models.ForeignKey(Brands, on_delete=models.CASCADE, verbose_name="Бренд")
    title = models.CharField(max_length=256, null=True, blank=True, verbose_name="Название товара")
    description = models.TextField(null=True, blank=True, verbose_name="Описание товара")
    mainimg = models.ImageField(upload_to="img/products/", null=True, blank=True, verbose_name="Главная картинка")
    stock_quantity = models.PositiveIntegerField(null=True, blank=True, default=0,
                                                 verbose_name="Количество товара (не обязательно для заполнения)")
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0,
                                           verbose_name="Процент скидки")
    # payment parameters
    package_code = models.CharField(max_length=256, null=True, blank=True, verbose_name="Код упаковки товара")
    code = models.CharField(max_length=256, null=True, blank=True, verbose_name="Код товара")
    price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True, verbose_name="Цена товара")
    vat_percent = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True, verbose_name="НДС")

    def __str__(self):
        return self.title

    def get_main_image_url(self):
        return self.mainimg.url if self.mainimg else None

    @property
    def discounted_price(self):
        try:
            if self.price is None or self.discount_percent is None:
                return self.price

            price = Decimal(self.price)
            discount_percent = Decimal(self.discount_percent)


            if discount_percent == Decimal(0):
                return 0

            discount = (price * discount_percent) / Decimal(100)
            final_price = price - discount

            #
            return final_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        except (InvalidOperation, TypeError, ValueError):

            return self.price

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class PopularProduct(BaseModel):
    product = models.ManyToManyField(Product, verbose_name="популярные товары")

    def __str__(self):
        return f"Группа популярных товаров"

    class Meta:
        verbose_name = "Популярные товары"
        verbose_name_plural = "Популярные товары"
