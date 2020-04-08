from django.urls import path, include
from api.controller import cardapio


urlpatterns = [
    path('cardapio', cardapio.get, name='cardapio'),
]