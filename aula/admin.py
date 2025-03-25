from django.contrib import admin
from aula.models import Passport, Person, Reporter, Article, Magazine

admin.site.register((Passport, Person, Reporter, Article, Magazine))

