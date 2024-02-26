from django.db import models
from abstractModels.abstractModel import BaseModel
from product.models import Product
from django.core.validators import FileExtensionValidator


class ProductIMG(BaseModel):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img/productIMG/',
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])

    def get_image_url(self):
        return self.img.url if self.img else None


