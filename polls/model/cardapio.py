from django.db import models
from django.utils import timezone
from polls.model.produto import Produto
from unicodedata import normalize

class Cardapio(models.Model):
    
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=4000)
    data_criacao = models.DateTimeField(default=timezone.now)
    produto = models.ManyToManyField(Produto, related_name='produtos')
    data_atualizacao = models.DateTimeField(default=None, blank=True, null=True)
    
    @classmethod
    def create(cls, titulo, descricao):
        produto = cls(titulo=titulo, descricao=descricao)
        return produto

    def publish(self):
            self.data_criacao = timezone.now()
            self.save()

    def __str__(self):
        return self.titulo
    
    def tag(self):
        return normalize('NFKD', self.titulo.lower()).encode('ASCII', 'ignore').decode('ASCII')