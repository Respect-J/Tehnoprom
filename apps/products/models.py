from django.db import models

from apps.brands.models import Brand
from apps.categories.models import Category
from models import BaseModel


class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    mainimg = models.ImageField(upload_to="img/products/", null=True, blank=True)
    stock_quantity = models.PositiveIntegerField(null=True, blank=True, default=0)
    # payment parameters
    package_code = models.CharField(max_length=256, null=True, blank=True)
    code = models.CharField(max_length=256, null=True, blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    vat_percent = models.DecimalField(max_digits=100, decimal_places=0, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_main_image_url(self):
        return self.mainimg.url if self.mainimg else None
