from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

@login_required
def getPage(request):
    conteudo = {
        'nome': 'Login'
    }
    return render(request, 'usuario/index.html', conteudo)