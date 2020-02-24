from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def getPageLogin(request):
    conteudo = {
        'nome': 'Login'
    }
    return render(request, 'usuario/usuario_login.html', conteudo)