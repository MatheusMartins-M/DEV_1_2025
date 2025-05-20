from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from aula.models import Exemplo


class SearchView(View):
    @staticmethod
    def get(request):
        try:
            resultados = {}
            query = request.GET.get('query')

            exemplos = Exemplo.objects.find_by_nome(query)

            if len(exemplos) == 0:
                raise Http404("Não tem exemplos")
            resultados_exemplos = []
            for exemplo in exemplos:
                url = "" #reverse_lazy("aula:exemplo_classe_read", kwargs={"pk"})
                resultados_exemplos.append((url, exemplo))
            resultados["Exemplo"] = resultados_exemplos
            context = {
                'results': resultados,
                'query': query,
            }
        except:
            context = {
                'query': query
            }

        return render(request, 'search/results.html', context)