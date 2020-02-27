from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

@login_required
def getPageCadastro(request):
    conteudo = {
        "Home": "Home"
    }
    return render(request, 'cliente/cliente.html', conteudo)