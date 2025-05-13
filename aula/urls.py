from django.urls import path
import aula.views as views_funcoes
from aula.views import *

app_name = 'aula'

urlpatterns = [
    path('funcao/teste', views_funcoes.primeira_view, name="Primeira_View"),
    path('funcao/saudacao', views_funcoes.saudacao, name="Saudacao"),
    path('funcao/<str:name>', views_funcoes.nome, name="nome"),

    path('classe/teste', PrimeiraView.as_view(), name="Primeira_View_Classe"),
    path('classe/saudacao', SaudacaoView.as_view(), name="Saudacao_View_Classe"),
    path('classe/<str:name>', NomeView.as_view(), name="Nome_View_Classe")
]