from django.db import models
from models import BaseModel


class Installment(BaseModel):
    title = models.CharField(max_length=256)
    logo = models.ImageField(upload_to="img/installment/")
    percent = models.FloatField(max_length=100, default=5)

    def __str__(self):
        return self.title
