from django.urls import path

from products.views import ProductDetailView, ProductListView, ProductCreateView

app_name = "products"
urlpatterns = [
    path('', ProductListView.as_view(), name="index"),
    path('<int:pk>', ProductDetailView.as_view(), name="detail"),
    path('<slug:slug>', ProductDetailView.as_view(), name="detail"),
    path('create/', ProductCreateView.as_view(), name="create"),
]