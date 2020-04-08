class ImagemViewModel():

    imagemJson = {
        'titulo': '',
        'url': '',
        'ordem': ''
    }
    
    imagemListaJson = []
    
    def montarItemJson(self,imagem):
        self.imagemJson['titulo'] = imagem.titulo
        self.imagemJson['url'] = imagem.url
        self.imagemJson['ordem'] = imagem.ordem
        return self.imagemJson
    
    def montaListaJson(self, imagemLista):
        for imagem in imagemLista:
            self.imagemListaJson.append(self.montarItemJson(imagem))
        return self.imagemListaJson