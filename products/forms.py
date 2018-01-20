from django import forms


class ProductAddForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField(max_digits=100, decimal_places=2)