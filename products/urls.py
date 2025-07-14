from django.urls import path

from products.views import update_product, products_list, delete_product, add_product, products_detail

app_name = 'products'

urlpatterns = [
    path('', products_list, name='list'),
    path('<int:pk>/', products_detail, name='detail'),
    path('add/', add_product, name='add'),
    path('update/<int:pk>/', update_product, name='update'),
    path('delete/<int:pk>/', delete_product, name='delete')
]
