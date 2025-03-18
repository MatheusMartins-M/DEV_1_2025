from django.utils.translation import gettext_lazy as _
from django.db import models

class TipoEsporte(models.TextChoices):
    CORRIDA = "RUN", _("Corrida")
    TRAIL_RUN = "TRUN", _("Corrida de Trilhas")
    BIKE = "BIK", _("Treino de Bicicleta")
    WALK = "WAL", _("Caminhada")
    HIIT = "HIT", _("Treino de Alta Intensidade")
    STRENGTH = "STR", _("Treino de Força")
    CARDIO = "CAR", _("Treino Aeróbico")
    SWIMMING = "SWM", _("Natação")