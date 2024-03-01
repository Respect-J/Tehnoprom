from django.db import models

from apps.collections.models import Collection
from models import BaseModel


class Category(BaseModel):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to="img/categories/", null=True, blank=True)

    def __str__(self):
        return self.title
