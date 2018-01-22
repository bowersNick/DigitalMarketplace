# Create your views here.
import os
from wsgiref.util import FileWrapper

from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from digitalmarketplace.mixins import MultiSlugMixin
from products.forms import ProductAddForm
from .models import Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductAddForm
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


class ProductDownloadView(MultiSlugMixin, DetailView):
    model = Product

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        filepath = os.path.join(settings.PROTECTED_ROOT, obj.media.path)
        wrapper = FileWrapper(open(filepath))
        response = HttpResponse(wrapper, content_type='application/force-download')
        """ Header information for the html """
        response["Content-Disposition"] = f"attachment; filename={obj.media.name}"
        response["X-SendFile"] = str(obj.media.name)
        return response
