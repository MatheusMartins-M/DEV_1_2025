from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from futebol.models.base_model import BaseModel

class Jogador(BaseModel):
    nome = models.CharField(
        null=False, blank=False,
        max_length=100,
        help_text="Digite o nome do jogador",
        verbose_name="Nome",
    )
    apelido = models.CharField(
        null=False, blank=False,
        max_length=100,
        help_text="Digite o apelido do jogador",
        verbose_name="Apelido",
    )
    data_nascimento = models.DateField(
        null=False, blank=False,
        default='',
        help_text="Digite a data",
        verbose_name="Data de nascimento"
    )
    numero_camisa = models.IntegerField(
        null=False, blank=False, unique=True,
        validators=[MinValueValidator(1), MaxValueValidator(99)],
        help_text="Digite o número da camisa",
        verbose_name="Número da camisa",
    )
    posicao = models.CharField(
        null=False, blank=False,
        max_length=100,
        help_text="Digite a posição do jogador",
        verbose_name="Posição do jogador",
    )
    qualidade = models.IntegerField(
        null=False, blank=False,
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        help_text="Digite a qualidade do jogador",
        verbose_name="Qualidade do jogador",
    )
    cartoes = models.IntegerField(
        null=False, blank=False,
        validators=[MinValueValidator(0), MaxValueValidator(3)],
        help_text="Digite a quantidade de cartões",
        verbose_name="Quantidade de cartões",
    )
    suspenso = models.BooleanField(
        default=False, null=False, blank=False,
        verbose_name = "Suspensão",
    )
