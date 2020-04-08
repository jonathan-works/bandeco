from api.view_model.produto_view_model import ProdutoViewModel

class CardapioViewModel():
    
    cardapioJson = {
        'titulo': '',
        'descricao': '',
        'produtos': []
    }

    cardapioListaJson = []
    
    def montarItemJson(self,cardapio):
        
        self.cardapioJson['titulo'] = cardapio.titulo
        self.cardapioJson['descricao'] = cardapio.descricao
        self.cardapioJson['produtos'] = ProdutoViewModel().montaListaJson(cardapio.produto.all())
        return self.cardapioJson
    
    def montaListaJson(self, cardapioLista):
        for cardapio in cardapioLista:
            self.cardapioListaJson.append(self.montarItemJson(cardapio))
        return self.cardapioListaJson