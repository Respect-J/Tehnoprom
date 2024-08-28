from django.contrib import admin

from .models import Product, PopularProduct

admin.site.register(Product)
admin.site.register(PopularProduct)

# Register your models here.
