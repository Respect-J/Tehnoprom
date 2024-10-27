from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from apps.collections.models import Collection
from models import BaseModel


class Category(BaseModel):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, verbose_name="Коллекция")
    title = models.CharField(max_length=256, verbose_name="Название")
    slug = models.SlugField(max_length=256, default="", blank=True, verbose_name=("Слаг"))
    img = models.ImageField(upload_to="img/categories/", null=True, blank=True, verbose_name="Картинка")
    seo_key = models.CharField(max_length=60, null=True, blank=True, verbose_name="Ключ слово для СЕО")
    title_key = models.CharField(max_length=60, null=True, blank=True, verbose_name="Title слово для СЕО")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"



def generate_unique_slug(instance, new_slug=None):
    slug = new_slug or slugify(instance.title)
    qs = Category.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        new_slug = f"{slug}-{qs.count() + 1}"
        return generate_unique_slug(instance, new_slug=new_slug)
    return slug


def pre_save_category_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = generate_unique_slug(instance)


pre_save.connect(pre_save_category_receiver, sender=Category)


class PopularCategory(BaseModel):
    categorys = models.ManyToManyField(Category, verbose_name="популярные категории")

    def __str__(self):
        return f"Группа популярных категория"

    class Meta:
        verbose_name = "Популярные категории"
        verbose_name_plural = "Популярные категории"
