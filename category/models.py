from django.db import models
from abstractModels.abstractModel import BaseModel
from collection.models import Collection


class Category(BaseModel):
    category = models.ForeignKey(Collection, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='img/category/', null=True, blank=True)

    def __str__(self):
        return self.title

