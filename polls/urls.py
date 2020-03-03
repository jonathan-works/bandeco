from django.urls import path, include

from .controller import home, usuario, cliente, sobre, produto

urlpatterns = [
    path('', home.getPage, name='home'),
    path('usuario', usuario.getPage, name='usuario'),
    path('cliente/cadastro', cliente.getPageCadastro, name='cliente.cadastro'),
    path('sobre', sobre.getPage , name='sobre'),
    path('produto/cadastro', produto.getPageCadastro , name='produto.cadastro'),
]