from django.db import models
from django.utils import timezone

class Cardapio(models.Model):
    
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=4000)
    data_criacao = models.DateTimeField(default=timezone.now)
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