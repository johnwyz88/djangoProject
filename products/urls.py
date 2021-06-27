from django.urls import path

from products.views import product_detail_view, product_delete_view, product_list_view
from products.views import product_create_view

app_name = 'products'
urlpatterns = [
    path('product/<int:id>/', product_detail_view, name="product-detail"),
    path('create/', product_create_view),
    path('product/<int:id>/delete/', product_delete_view, name="product-delete"),
    path('product/', product_list_view, name="product-list"),
]
