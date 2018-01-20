from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView

from products.forms import ProductAddForm
from .models import Product


class ProductCreateView(CreateView):
    model = Product
    fields = ["title", "description", "price"]
    # form_class = ProductAddForm()
    template_name = "product/create.html"
    # context_object_name = 'product'

    success_url = reverse_lazy('products:index')


class ProductDetailView(DetailView):
    model = Product
    template_name = "product/detail.html"
    context_object_name = 'product_detail'


class ProductListView(ListView):
    template_name = "product/index.html"
    context_object_name = 'product_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Product.objects.order_by('-price')[:5]
