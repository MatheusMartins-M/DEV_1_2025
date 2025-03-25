from django.db import models
from futebol.models.base_model import BaseModel

class Time(BaseModel):
    nome = models.CharField(
        null=False, blank=False,
        max_length=100,
        help_text="Digite o nome do time",
        verbose_name="Nome",
    )