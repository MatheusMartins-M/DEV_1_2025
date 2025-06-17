import random
import string
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView, UpdateView, CreateView, DetailView
from aula.forms import ExemploForm
from aula.models import Exemplo

@login_required
@permission_required("aula.view_exemplo", raise_exception=True)
def exemplo_detail(request, pk):
    exemplo = Exemplo.objects.get(id=pk)
    context = {
        'exemplo': exemplo,
    }
    return render(request, 'exemplo/read.html', context)

def exemplo_list(request):
    exemplos = Exemplo.objects.all()
    context = {
        'exemplos': exemplos,
    }

    return render(request, 'exemplo/list.html', context)

@login_required
@permission_required("aula.delete_exemplo")
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

@login_required
@permission_required("aula.add_exemplo")
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

@login_required
@permission_required("aula.change_exemplo")
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

@login_required
@permission_required("aula.generate_code_exemplo")
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

#=======================================================================================================================
#================================================ CLASSES ==============================================================
#=======================================================================================================================

class ExemploListView(View):
    @staticmethod
    def get (request):
        exemplos = Exemplo.objects.all()
        context = {
            'exemplos': exemplos,
        }

        return render(request, 'exemplo/list.html', context)

class ExemploDetailViewClasse(View):
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

class ExemploGenerateCodeView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = reverse_lazy('accounts:login')
    permission_required = 'aula.generate_code_exemplo'

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

class ExemploDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Exemplo
    fields = '__all__'
    template_name = "exemplo/read.html"
    success_url = reverse_lazy('aula:exemplo_class_list')
    permission_required = 'aula.view_exemplo'
    raise_exception = True

class ExemploDeleteView(LoginRequiredMixin, PermissionRequiredMixin, AccessMixin, DeleteView):
    model = Exemplo
    fields = '__all__'
    template_name = "exemplo/delete.html"
    success_url = reverse_lazy('aula:exemplo_class_list')
    permission_required = 'aula.delete_exemplo'
    raise_exception = True

class ExemploUpdateView(LoginRequiredMixin, PermissionRequiredMixin, AccessMixin, UpdateView):
    model = Exemplo
    #fields = '__all__'
    form_class = ExemploForm
    template_name = "exemplo/update.html"
    success_url = reverse_lazy('aula:exemplo_class_list')
    permission_required = 'aula.change_exemplo'
    raise_exception = True

class ExemploCreateView(LoginRequiredMixin, PermissionRequiredMixin, AccessMixin,  CreateView):
    model = Exemplo
    #fields = '__all__'
    form_class = ExemploForm
    template_name = "exemplo/create.html"
    success_url = reverse_lazy('aula:exemplo_class_list')
    permission_required = 'aula.add_exemplo'
    raise_exception = True