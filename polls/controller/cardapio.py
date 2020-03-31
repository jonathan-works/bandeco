from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from polls.model.cardapio import Cardapio

@login_required
def getPageCadastro(request):
    conteudo = {
        "titulo": "Cardapio"
    }
    
    return render(request, 'cardapio/cadastro.html', conteudo)
    

def postPageCadastro(request):
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo', '')
        descricao = request.POST.get('descricao', '')
        cardapio = Cardapio.create(titulo, descricao)
        cardapio.save()
    return render(request, 'cardapio/cadastro.html')

def getPageConsulta(request):

    titulo = request.GET.get('titulo', '')
    descricao = request.GET.get('descricao', '')
    
    querySet = Cardapio.objects

    if titulo != '':
        querySet = querySet.filter(titulo = titulo)
    if descricao != '':
        querySet = querySet.filter(descricao = descricao)
    else:
        querySet = querySet.all()

    cardapios = list(querySet)

    conteudo = {
        "titulo": "Cardapios",
        "cardapios": cardapios
    }
    
    return render(request, 'cardapio/consulta.html', conteudo)