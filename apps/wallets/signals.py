from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Wallet
from apps.users.models import UserModel


@receiver(post_save, sender=UserModel)
def create_user_wallet(sender, instance, created, **kwargs):

    if created:
        Wallet.objects.create(user=instance)
