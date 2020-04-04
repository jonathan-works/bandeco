from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from polls.model.produto import Produto


def getPage(request):

    #produtos = Produto.objects.all()

    produtos = Produto.objects.prefetch_related('imagens').all()

    conteudo = {
        "Titulo": "Home",
        "produtos": produtos
    }
     

    return render(request, 'index.html', conteudo)