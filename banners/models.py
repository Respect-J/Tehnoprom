from django.db import models
from abstractModels.abstractModel import BaseModel


class Banners(BaseModel):
    title_ru = models.CharField(max_length=256)
    title_en = models.CharField(max_length=256)
    img = models.ImageField(upload_to='img/banners/')

    def __str__(self):
        return self.title_ru

