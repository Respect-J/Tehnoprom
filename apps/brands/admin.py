from django.contrib import admin

from .models import BrandForCategory, Brands


admin.site.register(Brands)


class RequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category_id')
    search_fields = ('title', )
    list_filter = ('category_id', 'created_at')


admin.site.register(BrandForCategory, RequestAdmin)
