from django.core.validators import MinLengthValidator, MaxLengthValidator

from strava.enumerations.tipoesporte import TipoEsporte
from strava.models.base_model import BaseModel
from django.db import models

class Clube(BaseModel):
    nome = models.CharField(
        max_length=200, null=False, blank=False,
        validators=[MinLengthValidator(3), MaxLengthValidator(100)],
        help_text="Digite o nome",
        verbose_name="Nome",
    )
    local = models.CharField(
        null=False, blank=False,
        max_length=100,
        validators=[MinLengthValidator(3), MaxLengthValidator(100)],
        help_text="Digite o local",
        verbose_name="Local",
    )
    pais = models.CharField(
        null=False, blank=False,
        max_length=100,
        validators=[MinLengthValidator(3), MaxLengthValidator(100)],
        help_text="Digite o país",
        verbose_name="País",
    )
    tipo_esporte = models.CharField(
        max_length=5, null=False, blank=False,
        choices=TipoEsporte, default=0.0,
        help_text="Selecione o esporte",
        verbose_name="Esporte"
    )
    biografia = models.TextField(
        null=True, blank=True,
        help_text="Digite sua biografia (opcional)",
        verbose_name="Biografia",
    )
    url = models.URLField(
        null=False, blank=False,
        validators=[MinLengthValidator(15), MaxLengthValidator(150)],
        help_text="Digite a URL da pagina",
        verbose_name="URL",
    )

    def __str__(self):
        return self.nome