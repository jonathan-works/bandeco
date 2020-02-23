from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('home.html')
    context = {
        'data': 'Helo Wold'
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'home.html', context)