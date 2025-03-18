from django.utils.translation import gettext_lazy as _
from django.db import models

class Genero(models.TextChoices):
    MAN = "MAN", _("Homem")
    WOMAN = "WOM", _("Mulher")
    NON_BINARY = "NBI", _("Não-binário")
    NOT_INFORMED = "NIN", _("Não informado")