from django.urls import path

from .controller import home

urlpatterns = [
    path('', home.index, name='index'),
]