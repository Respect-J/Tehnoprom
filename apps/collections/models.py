from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.utils.translation import gettext_lazy as _

from models import BaseModel


class Collection(BaseModel):
    title = models.CharField(max_length=256, verbose_name=_("Название"))
    slug = models.SlugField(max_length=256, default="", blank=True, verbose_name=_("Слаг"))
    priority = models.IntegerField(default=1)
    img = models.ImageField(upload_to="img/collections/", null=True, blank=True, verbose_name=_("Картинка"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"


def generate_unique_slug(instance, new_slug=None):
    slug = new_slug or slugify(instance.title)
    qs = Collection.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        new_slug = f"{slug}-{qs.count() + 1}"
        return generate_unique_slug(instance, new_slug=new_slug)
    return slug


def pre_save_collection_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = generate_unique_slug(instance)


pre_save.connect(pre_save_collection_receiver, sender=Collection)
