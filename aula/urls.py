from django.urls import path
import aula.views as views_funcoes
from aula.views import *

app_name = 'aula'

urlpatterns = [
    path('funcao/teste', views_funcoes.primeira_view, name="Primeira_View"),
    path('classe/teste', PrimeiraView.as_view(), name="Primeira_View_Classe"),
    path('saudacao', views_funcoes.saudacao, name="Saudação")
]