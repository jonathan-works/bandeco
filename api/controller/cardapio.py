from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from polls.model.cardapio import Cardapio
from polls.model.produto import Produto

from api.view_model.cardapio_view_model import CardapioViewModel

def get(request):

    cardapios = Cardapio.objects.prefetch_related('produto').all()
    cv = CardapioViewModel()
    response = cv.montaListaJson(cardapios)
    
    return JsonResponse(response, safe=False)