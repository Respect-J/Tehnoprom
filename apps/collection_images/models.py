from django.core.validators import FileExtensionValidator
from django.db import models

from apps.products.models import Product
from models import BaseModel


class ProductIMG(BaseModel):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="выберите товар")
    img = models.ImageField(
        upload_to="img/productIMG/", null=True, validators=[FileExtensionValidator(["jpg", "jpeg", "png", "webp"])],
        verbose_name="Картинка"
    )

    def get_image_url(self):
        return self.img.url if self.img else None

    def __str__(self):
        return f"Доп. фото для товара {self.product_id.title}"

    class Meta:
        verbose_name = "Фото товара"
        verbose_name_plural = "Фото товаров"
