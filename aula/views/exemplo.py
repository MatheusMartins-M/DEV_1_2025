from django.shortcuts import render
from django.views import View
from aula.models import Exemplo

def exemplo_list(request):
    exemplos = Exemplo.objects.all()
    context = {
        'exemplos': exemplos,
    }

    return render(request, 'exemplo/list.html', context)

class ExemploListView(View):
    @staticmethod
    def get (request):
        exemplos = Exemplo.objects.all()
        context = {
            'exemplos': exemplos,
        }

        return render(request, 'exemplo/list.html', context)