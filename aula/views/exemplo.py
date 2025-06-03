from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView

from aula.models import Exemplo, Person

def exemplo_list(request):
    exemplos = Exemplo.objects.all()
    context = {
        'exemplos': exemplos,
    }

    return render(request, 'exemplo/list.html', context)

def exemplo_detail(request, pk):
    exemplo = Exemplo.objects.get(id=pk)
    context = {
        'exemplo': exemplo,
    }
    return render(request, 'exemplo/read.html', context)

def delete(request, exemplo_id):
    exemplo = get_object_or_404(Exemplo, pk=exemplo_id)
    try:
        if request.method == 'POST':
            v_exemplo_id = request.POST.get("exemplo_id", None)
            if int(v_exemplo_id) == exemplo_id:
                exemplo.delete()
                return redirect('aula:exemplo_function_list')
        else:
            context = {
                'exemplo' : exemplo,
            }
            return render(request, 'exemplo/delete.html', context)
    except:
        context = {}
        return render(request, 'exemplo/list.html', context)


class ExemploListView(View):
    @staticmethod
    def get (request):
        exemplos = Exemplo.objects.all()
        context = {
            'exemplos': exemplos,
        }

        return render(request, 'exemplo/list.html', context)

class ExemploDetailView(View):
    @staticmethod
    def get (request, pk):
        exemplo = Exemplo.objects.get(id=pk)
        context = {
            'exemplo': exemplo,
        }
        return render(request, 'exemplo/read.html', context)

class ExemploDeleteViewClass(View):
    @staticmethod
    def get(request, exemplo_id):
        exemplo = get_object_or_404(Exemplo, pk=exemplo_id)
        try:
            if request.method == 'POST':
                v_exemplo_id = request.POST.get("exemplo_id", None)
                if int(v_exemplo_id) == exemplo_id:
                    exemplo.delete()
                    return redirect('aula:exemplo_function_list')
            else:
                context = {
                    'exemplo' : exemplo,
                }
                return render(request, 'exemplo/delete.html', context)
        except:
            context = {}
            return render(request, 'exemplo/list.html', context)

class ExemploDeleteView(DeleteView):
    model = Exemplo
    filed = '__all__'
    template_name = "exemplo/delete.html"
    success_url = reverse_lazy('aula:exemplo_class_list')