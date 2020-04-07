from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from polls.model.cardapio import Cardapio
from polls.model.produto import Produto

@login_required
def getPageCadastro(request):
    conteudo = {
        "titulo": "Cadastro de Cardapio",
        "produtos": Produto.objects.prefetch_related('imagens').all()
    }
    
    return render(request, 'cardapio/cadastro.html', conteudo)
    

def postPageCadastro(request):
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo', '')
        descricao = request.POST.get('descricao', '')
        idProdutos = request.POST.getlist('produtos', [])
        cardapio = Cardapio.create(titulo, descricao)
        cardapio.save()

        if idProdutos != []:
            for idProduto in idProdutos:
                produto = Produto.objects.get(id=idProduto)
                cardapio.produto.add(produto)


    return getPageConsulta(request) #render(request, 'cardapio/cadastro.html')

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

def apagarCardapio(request, id):
   
    cardapio = Cardapio.objects.get(id=id)
    cardapio.delete()

    return getPageConsulta(request)