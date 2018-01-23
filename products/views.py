# Create your views here.
import os
from mimetypes import guess_type
from wsgiref.util import FileWrapper

from django.conf import settings
from django.http import HttpResponse, FileResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q

from digitalmarketplace.mixins import MultiSlugMixin
from products.forms import ProductAddForm
from .models import Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductAddForm
    success_url = reverse_lazy('products:index')

    def form_valid(self, form):
        # form.Meta.model.user_id = self.request.user.id
        f = form.save(commit=False)
        f.submitter_field = self.request.user
        f.save()
        super().form_valid(form)


class ProductDetailView(MultiSlugMixin, DetailView):
    model = Product


class ProductListView(ListView):
    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Product.objects.filter(Q(title__icontains=query)|Q(description__icontains=query))
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
        # print(response)
        guessed_type = guess_type(filepath)[0]
        mimetype = 'application/force-download'
        if guessed_type:
            mimetype = guessed_type
        response = FileResponse(open(filepath, 'rb'), content_type=mimetype)
        # """ Header information for the html """
        if not request.GET.get('preview'):
            response["Content-Disposition"] = f"attachment; filename={obj.media.name}"
        response["X-SendFile"] = str(obj.media.name)
        return response
