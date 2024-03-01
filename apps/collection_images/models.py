from django.core.validators import FileExtensionValidator
from django.db import models

from apps.products.models import Product
from models import BaseModel


class ProductIMG(BaseModel):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img/productIMG/', null=True, validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])

    def get_image_url(self):
        return self.img.url if self.img else None


