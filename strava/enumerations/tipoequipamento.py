from django.utils.translation import gettext_lazy as _
from django.db import models

class TipoEquipamento(models.TextChoices):
    SNEAKER = "TEN", _("Tênis")
    BIKE = "BIK", _("Bicicleta")
    SMART_DEVICE = "SDV", _("Dispositivo Inteligente")