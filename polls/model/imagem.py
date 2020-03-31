from django.db import models
from django.utils import timezone

class Imagem(models.Model):
    
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=4000)
    url = models.CharField(max_length=200)
    # ordem = models.IntegerField()
    data_criacao = models.DateTimeField(default=timezone.now)
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE, related_name='imagens')

    def publish(self):
            self.data_criacao = timezone.now()
            self.save()

    def __str__(self):
        return self.titulo