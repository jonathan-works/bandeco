from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def getPage(request):
    conteudo = {
        "Home": "Home"
    }
    return render(request, 'index.html', conteudo)