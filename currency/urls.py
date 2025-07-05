from django.urls import path
from currency.views import currency_view

app_name = 'currency'

urlpatterns = [
    path('', currency_view, name='currency')
]