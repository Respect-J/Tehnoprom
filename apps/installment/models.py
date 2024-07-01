from django.db import models
from models import BaseModel


class Installment(BaseModel):
    title = models.CharField(max_length=256)
    logo = models.ImageField(upload_to="img/installment/")
    percent = models.FloatField(max_length=100, default=5)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Рассрочка"
        verbose_name_plural = "Рассрочки"
