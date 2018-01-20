from django.contrib import admin

# Register your models here.
from .models import Product

""" can register just the model here, or, if additional properties need to be display, create an admin class like below
    and register this admin class along with the model class.
"""


class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "description", "price", "sale_price"]
    search_fields = ["description"]
    list_filter = ["price"]
    list_editable = ["sale_price"]
    exclude = ["slug"]
    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
