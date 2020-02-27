from django.urls import path, include

from .controller import home, usuario ,cliente

urlpatterns = [
    path('', home.getPage, name='home'),
    path('usuario', usuario.getPage, name='usuario'),
    path('cliente/cadastro', cliente.getPageCadastro, name='cliente.cadastro'),
]