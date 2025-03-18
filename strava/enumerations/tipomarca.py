from django.utils.translation import gettext_lazy as _
from django.db import models


class TipoMarca(models.TextChoices):
    CemMetros = "100M", _("100 metros")
    QuatrocentosMetros = "400M", _("400 metros")
    UmQuilometro = "1KM", _("1 Quilômetro")
    CincoQuilometros = "5KM", _("5 Quilômetros")
    DezQuilometros = "10KM", _("10 Quilômetros")
    QuinzeQuilometros = "15KM", _("15 Quilômetros")
    VinteQuilometros = "20KM", _("20 Quilômetros")
    MEIA = "MEIA", _("Meia maratona")
    TrintaQuilometros = "30KM", _("30 Quilômetros")
    maratona = "MARATONA", _("Maratona")
    LongaDist = "LONGA_DISTANCIA", _("Maior distância")
    LongaDur = "LONGA_DURACAO", _("Maior duração")