from django.core.validators import MinLengthValidator, MaxLengthValidator

from strava.enumerations.tipoesporte import TipoEsporte
from strava.models import BaseModel
from django.db import models

class Desafio(BaseModel):
    nome = models.CharField(
        null=False, blank=False,
        max_length=50,
        validators=[MinLengthValidator(5), MaxLengthValidator(50)],
        help_text="Nome do equipamento",
        verbose_name="Nome"
    )
    data_inicio = models.DateField(
        null=False, blank=False,
        help_text="Selecione o inicio",
        verbose_name="Inicio",
    )
    data_fim = models.DateField(
        null=False, blank=False,
        help_text="Selecione o inicio",
        verbose_name="Inicio",
    )
    tipo_esporte = models.CharField(
        max_length=5, null=False, blank=False,
        choices=TipoEsporte,
        help_text="Selecione o Esporte",
        verbose_name="Esporte",
    )
    visao_geral = models.TextField(
        null=False, blank=False,
        help_text="Digite o texto",
        verbose_name="Visão Geral",
    )
    selo = models.CharField(
        max_length=5, null=False, blank=False,
        help_text="Digite o selo",
        verbose_name="Selo",
    )

    def __str__(self):
        return self.nome

    class Meta:
        abstract = True
        app_label = "strava"