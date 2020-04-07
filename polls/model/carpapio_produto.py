# from django.db import models
# from django.utils import timezone
# from polls.model.cardapio import Cardapio
# from polls.model.produto import Produto

# class CardapioProduto(models.Model):
    
#     cardapio = models.ManyToManyField(Cardapio)
#     produto = models.ManyToManyField(Produto)
#     ordem = models.IntegerField()
#     data_criacao = models.DateTimeField(default=timezone.now)
#     data_atualizacao = models.DateTimeField(default=None, blank=True, null=True)
    
#     @classmethod
#     def create(cls, cardapio, produto, ordem=Produto.objects.count()+1):
#         produto = cls(cardapio=cardapio, produto=produto, ordem=ordem)
#         return produto

#     def publish(self):
#             self.data_criacao = timezone.now()
#             self.save()