from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from strava.enumerations.tipoesporte import TipoEsporte
from strava.models.base_model import BaseModel
from django.db import models

class Atividade(BaseModel):
    nome = models.CharField(
        null=False, blank=False,
        max_length=100,
        validators=[MinLengthValidator(5), MaxLengthValidator(100)],
        help_text="Nome da atividade",
        verbose_name="Nome"
    )
    observacoes = models.CharField(
        null=True, blank=True,
        max_length=100,
        validators=[MinLengthValidator(0), MaxLengthValidator(100)],
        help_text="Digite suas observações (Opcional)",
        verbose_name="Observações"
    )
    data = models.DateField(
        null=True, blank=True,
        help_text="Selecione a data",
        verbose_name="Data",
    )
    tipo_esporte = models.CharField(
        max_length=5, null=False, blank=False,
        choices=TipoEsporte, default="",
        help_text="Selecione o Esporte",
        verbose_name="Esporte",
    )
    inicio = models.TimeField(
        null=False, blank=False,
        help_text="Selecione o inicio",
        verbose_name="Inicio",
    )
    duracao = models.TimeField(
        null=False, blank=False,
        help_text="Selecione a duração",
        verbose_name="Duração",
    )
    distancia = models.FloatField(
        default=0.00, null=True, blank=True,
        help_text="Digite a distância percorrida",
        verbose_name="Distância",
    )
    ritmo = models.TimeField(
        null=True, blank=True,
        help_text="Selecione o ritmo",
        verbose_name="Ritmo",
    )
    calorias = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0,
        help_text="Calorias gastas",
        verbose_name="Calorias",
    )
    elevacao_total = models.IntegerField(
        default=0,
        help_text="Elevação total",
        verbose_name="Elevação",
    )
    def __str__(self):
        return self.nome