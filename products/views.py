# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from digitalmarketplace.mixins import MultiSlugMixin
from .models import Product


class ProductCreateView(CreateView):
    model = Product
    fields = ["title", "description", "price"]

    success_url = reverse_lazy('products:index')


class ProductDetailView(MultiSlugMixin, DetailView):
    model = Product


class ProductListView(ListView):
    def get_queryset(self):
        """Return the last five published questions."""
        return Product.objects.order_by('-price')  # [:5]


class ProductUpdateView(UpdateView):
    model = Product
    fields = ["title", "description", "price", "sale_price"]

    success_url = reverse_lazy('products:index')

    def get_context_data(self, *args, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(*args, **kwargs)
        context["submit_btn"] = "Update"
        return context


class ProductDeleteView(DeleteView):
    model = Product

    success_url = reverse_lazy('products:index')
