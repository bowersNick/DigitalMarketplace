from django import forms
from django.forms import Textarea, TextInput
from django.utils.text import slugify

from products.models import Product


class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price"
        ]
        widgets = {
            "description": Textarea(
                attrs={
                    "placeholder": "New Description",
                }
            ),
            "title": TextInput(
                attrs={
                    "placeholder": "Title",
                }
            ),
        }

    def clean(self):
        cleaned_data = super(ProductAddForm, self).clean()
        # title = cleaned_data.get("title")
        # slug = slugify(title)
        # qs = Product.objects.filter(slug=slug).exists()
        # if qs:
        #     raise forms.ValidationError("Title is taken, new title is needed.  Please try again.")
        return cleaned_data