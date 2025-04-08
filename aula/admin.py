from django.contrib import admin
from aula.models import Passport, Person, Reporter, Article, Magazine, Publication, Exemplo

admin.site.register((Passport, Person, Reporter, Article, Magazine, Publication, Exemplo))

