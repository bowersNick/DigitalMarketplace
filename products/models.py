from django.db import models

# Create your models here.
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2)
    sale_price = models.DecimalField(max_digits=100, decimal_places=2, null=True, default=0.0, blank=True)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.title


def product_pre_save_db(sender, instance, *args, **kwargs):
    if instance.slug != slugify(instance.title):
        instance.slug = slugify(instance.title)

pre_save.connect(product_pre_save_db, Product)