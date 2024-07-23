from django.db import models

from models import BaseModel


class Collection(BaseModel):
    title = models.CharField(max_length=256, null=True, blank=True,  verbose_name="Название")
    img = models.ImageField(upload_to="img/collections/", null=True, blank=True,  verbose_name="Картинка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "коллекция"
        verbose_name_plural = "коллекции"
