from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from polls.model.produto import Produto
from polls.model.cardapio import Cardapio


def getPage(request):

    #produtos = Produto.objects.all()
    produtoViewModel = {
        "id": '',
        'tiutlo': '',
        'descricao': '',
        'texto': '',
        'urlImgagemPrincipal': '',
        'urlImagensSecundarias': [],
        'cardapioTag': '',
        'preco': ''
    }

    produtos = []

    cardapiosProdutos = Cardapio.objects.prefetch_related('produto')

    for cardapioProduto in cardapiosProdutos:
        for produto in cardapioProduto.produto.all():
            produtoViewModel['id'] = produto.id
            produtoViewModel['titulo'] = produto.titulo
            produtoViewModel['descricao'] = produto.descricao
            produtoViewModel['texto'] = produto.texto
            produtoViewModel['urlImgagemPrincipal'] = produto.imagens.get()
            produtoViewModel['urlImagensSecundarias'] = produto.imagens.all()
            produtoViewModel['cardapioTag'] = cardapioProduto.tag
            produtoViewModel['preco'] = produto.preco      
        produtos.append(produtoViewModel)



            # produto.id = cardapioProduto.produtos
            # produtos.append(produto)

    # for p in cardapiosProdutos:
    #     print(p.produto.all())
    cardapios = cardapiosProdutos.all()
    # produtos = Produto.objects.prefetch_related('imagens').all()

    
    conteudo = {
        "Titulo": "Home",
        "produtos": produtos,
        "cardapios": cardapios        
    }
     
    return render(request, 'index.html', conteudo)