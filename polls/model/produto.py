from django.db import models
from django.utils import timezone

class Produto(models.Model):
    
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=4000)
    texto = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    # ordem = models.IntegerField()
    data_criacao = models.DateTimeField(default=timezone.now)
    data_atualizacao = models.DateTimeField(default=None, blank=True, null=True)
    
    
    @classmethod
    def create(cls, titulo, descricao, texto, preco):
        produto = cls(titulo=titulo, descricao=descricao, texto=texto, preco=preco)
        return produto

    def publish(self):
            self.data_criacao = timezone.now()
            self.save()

    def __str__(self):
        return self.titulo