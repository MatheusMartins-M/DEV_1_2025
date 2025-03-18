from strava.models.desafio import Desafio
from django.db import models

class DesafioTempo(Desafio):
    meta_duracao = models.TimeField(
        null=False, blank=False,
        help_text="Digite a meta",
        verbose_name="Meta",
    )

    def __str__(self):
        return f'{self.nome} -(tempo) {self.meta_duracao}'

