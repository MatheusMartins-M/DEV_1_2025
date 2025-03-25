from django.core.validators import MinValueValidator
from django.db import models
from aula.models.base_model import BaseModel

class Magazine(BaseModel):
    title = models.CharField(
        null=False, blank=False,
        max_length=100,
        help_text="Digite o nome",
        verbose_name="Nome",
    )
    edition = models.IntegerField(
        null=False, blank=False, default="1",
        validators=[MinValueValidator(1)],
        help_text = "Digite qual a edição",
        verbose_name = "Edição",
    )

    def __str__(self):
        return f'{self.title}'