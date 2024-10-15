from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserModel
import django.contrib.auth.models
from django.contrib import auth

admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)


@admin.register(UserModel)
class CustomUserAdmin(UserAdmin):
    fieldsets = None
    fields = [
        "username",
        "password",
        "first_name",
        "last_name",
        "is_active",
        "is_phone_verified",
        "phone_number"
    ]
