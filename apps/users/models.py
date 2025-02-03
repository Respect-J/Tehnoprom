from django.contrib.auth.models import AbstractBaseUser, User
from django.db import models
from django.utils import timezone
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
    # Поля для премиума
    is_premium = models.BooleanField(default=False, help_text="Флаг наличия премиум-аккаунта.")
    premium_end_date = models.DateTimeField(null=True, blank=True, help_text="Дата окончания премиум-подписки.")


    def __str__(self):
        return self.username

    def check_and_update_premium_status(self):
        """
        Проверяет, не истекла ли дата премиум-подписки. Если истекла,
        сбрасывает флаг is_premium и сохраняет модель.
        """
        if self.is_premium and self.premium_end_date and self.premium_end_date < timezone.now():
            self.is_premium = False
            self.save()

    def get_main_image_url(self):
        return self.mainimg.url if self.mainimg else None

    class Meta:
        db_table = "users"
