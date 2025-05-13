from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.core.serializers import serialize
from datetime import datetime
from django.views import View
from aula.models import Exemplo

def primeira_view(request):
    mensagem = "Boa noite Dev 1"
    #return HttpResponse(mensagem, status=200)
    return render(request, 'primeira.html', {'mensagem':mensagem})

class PrimeiraView(View):
    @staticmethod
    def get (request):
        mensagem = request.META["REMOTE_ADDR"]
        return HttpResponse(mensagem, status=200)

def saudacao(request):
    agora = datetime.now()
    mensagem = "Boa noite"
    if 12 > agora.hour > 6:
        mensagem = "Bom dia"
    elif 0 < agora.hour <= 6:
        mensagem = "Boa madrugada"

    completo = f"<html><body><h1>{mensagem.capitalize()} visitante!" \
                f"<br />{agora} </h1></body></html>"
    return HttpResponse(completo)

class SaudacaoView(View):
    @staticmethod
    def get(request):
        agora = datetime.now()
        mensagem = "Boa noite"
        if 12 > agora.hour > 6:
            mensagem = "Bom dia"
        elif 0 < agora.hour <= 6:
            mensagem = "Boa madrugada"

        completo = f"<html><body><h1>{mensagem.capitalize()} visitante!" \
                   f"<br />{agora} </h1></body></html>"
        return HttpResponse(completo)

def nome(request, name):
    exemplo = Exemplo.objects.find_by_nome(name)
    #context = {'message':name}
    return HttpResponse(exemplo[0], status=200)

class NomeView(View):
    @staticmethod
    def get(request, name):
        exemplo = Exemplo.objects.find_by_nome(name)
        # context = {'message':name}
        return HttpResponse(exemplo[0], status=200)