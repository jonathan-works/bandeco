from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def getPage(request):
    conteudo = {
        'nome': 'Login'
    }
    return render(request, 'usuario/index.html', conteudo)