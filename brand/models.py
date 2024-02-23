from django.db import models
from abstractModels.abstractModel import BaseModel


class Brand(BaseModel):
    title = models.CharField(max_length=256, null=True, blank=True)
    logo = models.ImageField(upload_to='img/brand/', null=True, blank=True)

    def __str__(self):
        return self.title

