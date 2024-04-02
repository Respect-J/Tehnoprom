from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserModel


@admin.register(UserModel)
class CustomUserAdmin(UserAdmin):
    fieldsets = None
    fields = [
        "username",
        "password",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "user_permissions",
        "groups",
    ]
