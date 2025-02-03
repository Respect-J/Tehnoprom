from celery import shared_task
from django.utils import timezone
from .models import UserModel

@shared_task
def check_expired_premium():
    """
    Проверяет всех пользователей, у кого is_premium=True,
    и если premium_end_date < текущего времени, сбрасывает is_premium.
    """
    now = timezone.now()
    # Выбираем всех, у кого премиум просрочен
    expired_users = UserModel.objects.filter(is_premium=True, premium_end_date__lt=now)
    expired_users.update(is_premium=False)