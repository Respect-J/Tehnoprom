from django.contrib import admin

from .models import Product, PopularProduct, DayProduct
from apps.characteristics.models import Characteric
from apps.collection_images.models import ProductIMG


@admin.register(PopularProduct)
class PopularProductAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):

        return not PopularProduct.objects.exists()


@admin.register(DayProduct)
class DayProductAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):

        return not DayProduct.objects.exists()


class CharactericInline(admin.StackedInline):
    model = Characteric
    extra = 1



class ProductIMGInline(admin.TabularInline):
    model = ProductIMG
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'brandcategory', 'brands', 'price')
    list_filter = ('category', 'brandcategory', 'brands',)
    search_fields = ('title',)
    inlines = [CharactericInline, ProductIMGInline]
