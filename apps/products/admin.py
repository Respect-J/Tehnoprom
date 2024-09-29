from django.contrib import admin

from .models import Product, PopularProduct, DayProduct

admin.site.register(Product)
admin.site.register(PopularProduct)
admin.site.register(DayProduct)

# Register your models here.
