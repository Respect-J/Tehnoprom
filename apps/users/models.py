from django.contrib.auth.models import AbstractBaseUser, User
from django.db import models

from models import BaseModel


class UserModel(User):
    is_superuser = False
    is_staff = False

    mainimg = models.ImageField(upload_to="users/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    verification_code = models.CharField(max_length=6, null=True, blank=True)
    is_phone_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def get_main_image_url(self):
        return self.mainimg.url if self.mainimg else None

    class Meta:
        db_table = "users"
