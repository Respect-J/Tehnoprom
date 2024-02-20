from django.db import models
from abstractModels.abstractModel import BaseModel


class Collection(BaseModel):
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='img/collection/', null=True, blank=True)

    def __str__(self):
        return self.title


