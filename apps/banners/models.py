from django.db import models

from models import BaseModel


class Banner(BaseModel):
    title_ru = models.CharField(max_length=256, verbose_name="Название на русском")
    img = models.ImageField(upload_to="img/banners/", verbose_name="Изображение")

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"
