from django.urls import path, include

from .controller import home, usuario, cliente, sobre, produto, cardapio

urlpatterns = [
    path('', home.getPage, name='home'),
    path('usuario', usuario.getPage, name='usuario'),
    path('cliente/cadastro', cliente.getPageCadastro, name='cliente.cadastro'),
    path('sobre', sobre.getPage , name='sobre'),

    path('produto/cadastro/post', produto.postPageCadastro , name='produto.cadastro.cadastro'),
    path('produto/cadastro', produto.getPageCadastro , name='produto.cadastro'),

    path('produto/consulta', produto.getPageConsulta , name='produto.consulta'),
    # path('produto/editar', produto.getPageCadastro , name='produto.cadastro')


    path('cardapio/cadastro/post', cardapio.postPageCadastro , name='cardapio.cadastro.cadastro'),
    path('cardapio/cadastro', cardapio.getPageCadastro , name='cardapio.cadastro'),
    
    path('cardapio/consulta', cardapio.getPageConsulta , name='cardapio.consulta'),
    # path('cardapio/editar', produto.getPageCadastro , name='produto.cadastro')
]