from django.contrib import admin
from django.contrib.auth.models import User

from .models import UserModel

admin.site.unregister(User)


@admin.register(User)
class BaseUserAdmin(admin.ModelAdmin):
    fields = [
        "username",
        "password",
        "first_name",
        "last_name",
        "email",
        "is_superuser",
        "is_active",
        "is_staff",
        "user_permissions",
        "groups",
    ]


@admin.register(UserModel)
class CustomUserAdmin(admin.ModelAdmin):
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
