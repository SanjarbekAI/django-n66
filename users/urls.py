from django.urls import path

from users.views import index_view

app_name = 'users'

urlpatterns = [
    path('home/', index_view, name='home'),
]
