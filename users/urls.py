from django.urls import path

from users.views import index_view

urlpatterns = [
    path('home/', index_view),
]
