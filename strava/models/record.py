from strava.enumerations.tipoesporte import TipoEsporte
from strava.enumerations.tipomarca import TipoMarca
from strava.models.base_model import BaseModel
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

class Record(BaseModel):
    nome = models.CharField(
        null=False, blank=False,
        max_length=20,
        validators = [MinLengthValidator(2), MaxLengthValidator(20)],
        help_text = "Nome para o record",
        verbose_name = "Nome"
    )
    tipo_marca = models.CharField(
        max_length=15, null=False, blank=False,
        choices=TipoMarca, default=0.0,
        help_text = "Selecione sua marca",
        verbose_name = "Marca"
    )
    tipo_esporte = models.CharField(
        max_length=5, null=False, blank=False,
        choices=TipoEsporte, default=0.0,
        help_text="Selecione seu esporte",
        verbose_name="Esporte"
    )
    ritmo = models.TimeField(
        null=False, blank=False,
        help_text="Digite o ritmo",
        verbose_name="Ritmo"
    )
    duracao = models.TimeField(
        null=False, blank=False,
        help_text = "Digite a duração",
        verbose_name = "Duração"
    )

    def __str__(self):
        return self.nome