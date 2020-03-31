from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from polls.model.produto import Produto

@login_required
def getPageCadastro(request):
    conteudo = {
        "titulo": "Home"
    }
    
    return render(request, 'produto/cadastro.html', conteudo)
    

def postPageCadastro(request):
    
    data = {}
    
    if request.method == 'POST':
        data['titulo'] = request.POST.get('titulo', '')
        data['descricao'] = request.POST.get('descricao', '') 
        data['texto'] = request.POST.get('texto', '')
        data['preco'] = request.POST.get('preco', 0)
        produto = Produto.create(data['titulo'], data['descricao'], data['texto'], data['preco'])
        produto.save()
    return render(request, 'produto/cadastro.html')

def getPageConsulta(request):

    titulo = request.GET.get('titulo', '')
    descricao = request.GET.get('descricao', '')
    preco = request.GET.get('preco', '')
    
    querySet = Produto.objects

    if titulo != '':
        querySet = querySet.filter(titulo = titulo)
    if descricao != '':
        querySet = querySet.filter(descricao = descricao)
    if preco != '':
        querySet = querySet.filter(preco = preco)
    else:
        querySet = querySet.all()

    produtos = list(querySet)

    conteudo = {
        "titulo": "Produtos",
        "produtos": produtos
    }
    
    return render(request, 'produto/consulta.html', conteudo)