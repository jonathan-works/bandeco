from django.urls import path

from .controller import home, usuario

urlpatterns = [
    path('', home.getPage, name='home'),
    path('login', usuario.getPageLogin, name='login'),
]