from django.shortcuts import render
from django.http import HttpResponse


def getPage(request):
    conteudo = {
        "sobre": "Home"
    }
    return render(request, 'sobre.html', conteudo)