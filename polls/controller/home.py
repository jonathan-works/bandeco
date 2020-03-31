from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from polls.model.produto import Produto


def getPage(request):

    produtos = list(Produto.objects.all())

    conteudo = {
        "Titulo": "Home",
        "produtos": produtos
    }

    return render(request, 'index.html', conteudo)