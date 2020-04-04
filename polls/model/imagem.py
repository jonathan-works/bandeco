from django.db import models
from django.utils import timezone

class Imagem(models.Model):
    
    titulo = models.CharField(max_length=200, null=False)
    url = models.CharField(max_length=200, null=False)
    ordem = models.IntegerField(null=False)
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE, related_name='imagens')
    data_criacao = models.DateTimeField(default=timezone.now)

    @classmethod
    def create(cls, titulo, ordem, url, produto):
        imagem = cls(titulo=titulo, ordem=ordem, url=url, produto=produto)
        return imagem

    def publish(self):
            self.data_criacao = timezone.now()
            self.save()

    def __str__(self):
        return self.url