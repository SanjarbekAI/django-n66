from django.urls import path

from products.views import update_product, products_list, delete_product, add_product

app_name = 'products'

urlpatterns = [
    path('', products_list, name='list'),
    path('add/', add_product, name='add'),
    path('update/<int:product_id>/', update_product, name='update'),
    path('delete/<int:product_id>/', delete_product, name='delete')
]
