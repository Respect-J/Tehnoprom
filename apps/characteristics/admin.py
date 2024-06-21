from django.contrib import admin
from .models import Characteric, CharacteristicItem


class CharacteristicItemInline(admin.TabularInline):
    model = CharacteristicItem
    extra = 1


class CharactericAdmin(admin.ModelAdmin):
    inlines = [CharacteristicItemInline]


admin.site.register(Characteric, CharactericAdmin)
admin.site.register(CharacteristicItem)
