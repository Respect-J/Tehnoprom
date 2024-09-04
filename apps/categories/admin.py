from django.contrib import admin

from .models import Category, PopularCategory

admin.site.register(Category)
admin.site.register(PopularCategory)