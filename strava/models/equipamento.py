from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator

from strava.enumerations.tipoequipamento import TipoEquipamento
from strava.enumerations.tipoesporte import TipoEsporte
from strava.models.base_model import BaseModel
from django.db import models

class Equipamento(BaseModel):
    nome = models.CharField(
        null=False, blank=False,
        max_length=50,
        validators=[MinLengthValidator(2), MaxLengthValidator(50)],
        help_text="Nome do equipamento",
        verbose_name="Nome"
    )
    marca = models.CharField(
        null=False, blank=False,
        max_length=50,
        validators=[MinLengthValidator(2), MaxLengthValidator(50)],
        help_text="Marca do equipamento",
        verbose_name="Marca"
    )
    modelo = models.CharField(
        null=False, blank=False,
        max_length=50,
        validators=[MinLengthValidator(2), MaxLengthValidator(50)],
        help_text="Modelo do equipamento",
        verbose_name="Modelo"
    )
    apelido = models.CharField(
        null=False, blank=False,
        max_length=50,
        validators=[MinLengthValidator(2), MaxLengthValidator(50)],
        help_text="Apelido do equipamento",
        verbose_name="Apelido"
    )
    tipo_equipamento = models.CharField(
        max_length=5, null=False, blank=False,
        choices=TipoEquipamento, default="",
        help_text="Selecione o tipo do equipamento",
        verbose_name="Equipamento",
    )
    tipo_esporte = models.CharField(
        max_length=5, null=False, blank=False,
        choices=TipoEsporte, default="",
        help_text="Selecione o Esporte",
        verbose_name="Esporte",
    )
    distancia_total = models.FloatField(
        validators=[MinValueValidator(0)],
        null=True, blank=True,
        help_text="Distancia total",
        verbose_name="Distancia total"
    )
    distancia_prevista = models.IntegerField(
        validators=[MinValueValidator(400)],
        null=False, blank=False,
        help_text="Distancia prevista",
        verbose_name="Distancia prevista"
    )
    peso = models.FloatField(
        validators=[MinValueValidator(0)],
        null=True, blank=True,
        help_text="Digite seu peso",
        verbose_name="Peso",
    )
    notas = models.TextField(
        null=True, blank=True,
        help_text="Digite sua biografia (opcional)",
        verbose_name="Biografia",
    )

    def __str__(self):
        return self.nome