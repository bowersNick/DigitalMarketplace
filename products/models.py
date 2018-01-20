from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2)
    sale_price = models.DecimalField(max_digits=100, decimal_places=2, null=True, default=0.0, blank=True)

    def __str__(self):
        return self.title