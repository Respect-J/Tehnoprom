from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from apps.categories.models import Category
from models import BaseModel


class BrandForCategory(BaseModel):
    title = models.CharField(max_length=256, verbose_name="Название на русском")
    slug = models.SlugField(max_length=256, default="", blank=True, verbose_name=("Слаг"))
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="категория")
    logo = models.ImageField(upload_to="img/brands/", null=True, blank=True, verbose_name="Логотип")
    seo_key = models.CharField(max_length=60, null=True, blank=True, verbose_name="Ключ слово для СЕО")
    title_key = models.CharField(max_length=60, null=True, blank=True, verbose_name="Title слово для СЕО")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


def generate_unique_slug(instance, new_slug=None):
    slug = new_slug or slugify(instance.title)
    qs = BrandForCategory.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        new_slug = f"{slug}-{qs.count() + 1}"
        return generate_unique_slug(instance, new_slug=new_slug)
    return slug


def pre_save_brand_for_category_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = generate_unique_slug(instance)


pre_save.connect(pre_save_brand_for_category_receiver, sender=BrandForCategory)


class Brands(BaseModel):
    title = models.CharField(max_length=256, verbose_name="Название на русском")
    slug = models.SlugField(max_length=256, default="", blank=True, verbose_name=("Слаг"))
    logo = models.ImageField(upload_to="img/brands/", null=True, blank=True, verbose_name="Логотип")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

# Генерация уникального slug для Brands
def generate_unique_slug_for_brands(instance, new_slug=None):
    slug = new_slug or slugify(instance.title)
    qs = Brands.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        new_slug = f"{slug}-{qs.count() + 1}"
        return generate_unique_slug_for_brands(instance, new_slug=new_slug)
    return slug

def pre_save_brands_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = generate_unique_slug_for_brands(instance)

pre_save.connect(pre_save_brands_receiver, sender=Brands)
