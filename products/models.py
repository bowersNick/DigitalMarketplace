from django.conf import settings
from django.db import models

# Create your models here.
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2)
    sale_price = models.DecimalField(max_digits=100, decimal_places=2, null=True, default=0.0, blank=True)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.title


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def product_pre_save_db(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(product_pre_save_db, sender=Product)