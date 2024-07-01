from django.db import models
from apps.categories.models import Category
from models import BaseModel


class Brand(BaseModel):
    title = models.CharField(max_length=256, null=True, blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    logo = models.ImageField(upload_to="img/brands/", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренд"
