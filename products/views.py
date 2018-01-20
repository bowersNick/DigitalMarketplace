from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView


class ProductView(DetailView):
    template_name = "product/index.html"