from api.view_model.imagem_view_model import ImagemViewModel

class ProdutoViewModel():
    
    produtoJson = {
        'titulo': '',
        'descricao': '',
        'texto': '',
        'preco': '',
        'imagens': []
    }

    produtoListaJson = []
    
    def montarItemJson(self,produto):
        self.produtoJson['titulo'] = produto.titulo
        self.produtoJson['descricao'] = produto.descricao
        self.produtoJson['texto'] = produto.texto
        self.produtoJson['preco'] = produto.preco
        self.produtoJson['imagens'] = ImagemViewModel().montaListaJson(produto.imagens.all())
        return self.produtoJson
    
    def montaListaJson(self, produtoLista):
        for produto in produtoLista:
            self.produtoListaJson.append(self.montarItemJson(produto))
        return self.produtoListaJson