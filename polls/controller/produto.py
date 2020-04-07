from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from polls.model.produto import Produto
from polls.model.imagem import Imagem
from polls.model.upload_file_form import UploadFileForm
from django.core.files.storage import FileSystemStorage


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@login_required
def getPageCadastro(request):
    conteudo = {
        "titulo": "Cadastro de Produto"
    }
    
    return render(request, 'produto/cadastro.html', conteudo)
    
def postPageCadastro(request):
    
    if request.method == 'POST':
        title = request.POST.get('titulo', '')
        descricao = request.POST.get('descricao', '') 
        texto = request.POST.get('texto', '')
        preco = request.POST.get('preco', 0)

        produto = Produto.create(title, descricao, texto, preco)
        produto.save()

        uploaded_file = request.FILES['imagem']
        fileSystemStorage = FileSystemStorage()
        filename  = fileSystemStorage.save(uploaded_file.name, uploaded_file)

        imagem = Imagem.create(uploaded_file.name, 1, fileSystemStorage.url(filename), produto)
        imagem.save()

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

def apagarProduto(request, id):

   
    produto = Produto.objects.get(id=id)
    produto.delete()

    return getPageConsulta(request)
