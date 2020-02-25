from django.urls import path, include

from .controller import home, usuario

urlpatterns = [
    path('', home.getPage, name='home'),
    path('usuario', usuario.getPage, name='usuario')
]