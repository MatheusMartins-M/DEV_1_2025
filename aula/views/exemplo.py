import random
import string

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView, UpdateView, CreateView

from aula.forms import ExemploForm
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

def create(request):
    if request.method == "POST":
        form = ExemploForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aula:exemplo_function_list')
    else:
        form = ExemploForm()
    context = {
        'form' : form
    }
    return render (request, 'exemplo/create.html', context)

def update(request, exemplo_id):
    exemplo = get_object_or_404(Exemplo, pk=exemplo_id)
    if request.method == "POST":
        form = ExemploForm(request.POST, instance=exemplo)
        if form.is_valid():
            form.save()
            return redirect('aula:exemplo_function_list')
    else:
        form = ExemploForm(instance=exemplo)
    context = {
        'form' : form,
        'exemplo': exemplo,
    }
    return render (request, 'exemplo/update.html', context)

def generate_code(request, exemplo_id):
    exemplo = get_object_or_404(Exemplo, pk=exemplo_id)
    try:
        letters = string.ascii_letters + string.digits
        exemplo.cod = ''.join(random.choice(letters) for i in range(10))
        exemplo.save()
        return redirect('aula:exemplo_function_list')
    except:
        # TODO: Tratar erro, pode ser gerada uma mensagem para onde será renderizado
        print(f"Erro ao gerar código para exemplo {exemplo}")
        return redirect('aula:exemplo_function_list')

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


class ExemploCreateViewClass(View):
    @staticmethod
    def get(request):
        if request.method == "POST":
            form = ExemploForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('aula:exemplo_function_list')
        else:
            form = ExemploForm()
        context = {
            'form': form
        }
        return render(request, 'exemplo/create.html', context)

class ExemploUpdateViewClass(View):
    @staticmethod
    def get(request, pk):
        exemplo = get_object_or_404(Exemplo, pk=pk)
        if request.method == "POST":
            form = ExemploForm(request.POST, instance=exemplo)
            if form.is_valid():
                form.save()
                return redirect('aula:exemplo_function_list')
        else:
            form = ExemploForm(instance=exemplo)
        context = {
            'form' : form,
            'exemplo': exemplo,
        }
        return render (request, 'exemplo/update.html', context)

class ExemploGenerateCodeView(View):
    @staticmethod
    def get(request, pk):
        exemplo = get_object_or_404(Exemplo, pk=pk)
        try:
            letters = string.ascii_letters + string.digits
            exemplo.cod = ''.join(random.choice(letters) for i in range(10))
            exemplo.save()
            return redirect('aula:exemplo_function_list')
        except:
            # TODO: Tratar erro, pode ser gerada uma mensagem para onde será renderizado
            print(f"Erro ao gerar código para exemplo {exemplo}")
            return redirect('aula:exemplo_function_list')

class ExemploDeleteView(DeleteView):
    model = Exemplo
    fields = '__all__'
    template_name = "exemplo/delete.html"
    success_url = reverse_lazy('aula:exemplo_class_list')

class ExemploUpdateView(UpdateView):
    model = Exemplo
    #fields = '__all__'
    form_class = ExemploForm
    template_name = "exemplo/update.html"
    success_url = reverse_lazy('aula:exemplo_class_list')

class ExemploCreateView(CreateView):
    model = Exemplo
    #fields = '__all__'
    form_class = ExemploForm
    template_name = "exemplo/create.html"
    success_url = reverse_lazy('aula:exemplo_class_list')