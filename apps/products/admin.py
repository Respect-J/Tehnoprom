from django.contrib import admin

from .models import Product, PopularProduct, DayProduct

admin.site.register(Product)


@admin.register(PopularProduct)
class PopularProductAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):

        return not PopularProduct.objects.exists()


@admin.register(DayProduct)
class DayProductAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):

        return not DayProduct.objects.exists()

