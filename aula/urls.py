from django.urls import path
import aula.views as views_funcoes
from aula.views import *

app_name = 'aula'

urlpatterns = [
    path('funcao/teste', views_funcoes.primeira_view, name="Primeira_View"),
    path('funcao/saudacao', views_funcoes.saudacao, name="Saudacao"),
    path('funcao/<str:name>', views_funcoes.nome, name="nome"),
    path('exemplo/function', views_funcoes.exemplo_list, name="exemplo_function_list"),
    path('exemplo/function/read/<int:pk>', views_funcoes.exemplo_detail, name="exemplo_function_read"),                 #<int:pk> e
    path('exemplo/function/delete/<int:exemplo_id>', views_funcoes.delete, name="exemplo_function_delete"),             #<int:exemplo_id> são a mesma coisa, não importa o nome
    path('exemplo/function/create', views_funcoes.create, name="exemplo_function_create"),
    path('exemplo/function/update/<int:exemplo_id>', views_funcoes.update, name="exemplo_function_update"),
    path('exemplo/function/gerar_codigo/<int:exemplo_id>', views_funcoes.generate_code, name="exemplo_function_generate_code"),

    path('classe/teste', PrimeiraView.as_view(), name="Primeira_View_Classe"),
    path('classe/saudacao', SaudacaoView.as_view(), name="Saudacao_View_Classe"),
    path('classe/<str:name>', NomeView.as_view(), name="Nome_View_Classe"),
    path('exemplo/classe', ExemploListView.as_view(), name="exemplo_class_list"),
    path('exemplo/classe/read/<int:pk>', ExemploDetailView.as_view(), name="exemplo_classe_read"),
    path('exemplo/classe/delete/<int:pk>', ExemploDeleteView.as_view(), name="exemplo_classe_delete"),
    path('exemplo/classe/create', ExemploCreateView.as_view(), name="exemplo_classe_create"),
    path('exemplo/classe/update/<int:pk>', ExemploUpdateView.as_view(), name="exemplo_classe_update"),
    path('exemplo/classe/gerar_codigo/<int:pk>', ExemploGenerateCodeView.as_view(), name="exemplo_classe_generate_code"),
]