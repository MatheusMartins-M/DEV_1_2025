from django.contrib import admin
from strava.models import Atividade, Clube, Equipamento, Perfil, Record, DesafioTempo

admin.site.register((Atividade, Clube, Equipamento, Perfil, Record, DesafioTempo))