from django.urls import path

from products.views import ProductDetailView, ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = "products"
urlpatterns = [
    path('', ProductListView.as_view(), name="index"),
    path('<int:pk>', ProductDetailView.as_view(), name="detail"),
    path('<slug:slug>', ProductDetailView.as_view(), name="detail"),
    path('create/', ProductCreateView.as_view(), name="create"),
    path('<int:pk>/edit', ProductUpdateView.as_view(), name="update"),
    path('<slug:slug>/edit', ProductUpdateView.as_view(), name="update"),
    path('<int:pk>/delete', ProductDeleteView.as_view(), name="delete"),
    path('<slug:slug>/delete', ProductDeleteView.as_view(), name="delete"),
]