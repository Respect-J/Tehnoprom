from django.db import models
from models import BaseModel


class Installment(BaseModel):
    title = models.CharField(max_length=256,  verbose_name="Название рассрочки")
    logo = models.ImageField(upload_to="img/installment/",  verbose_name="Логотип рассрочки")
    percent = models.FloatField(max_length=100, default=5, verbose_name="Процент рассрочки")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Рассрочка"
        verbose_name_plural = "Рассрочки"
