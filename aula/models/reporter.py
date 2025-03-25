from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from aula.models.base_model import BaseModel

class Reporter(BaseModel):
    name = models.CharField(
        null=False, blank=False,
        max_length=100,
        help_text="Digite o nome",
        verbose_name="Nome",
    )
    email = models.EmailField(
        max_length=254, null=False, blank=False, unique=True,
        help_text="Email exemplo",
        verbose_name="E-mail",
    )
    cpf = models.CharField(
        null=False, blank=False,
        max_length=11,
        validators=[MinLengthValidator(11), MaxLengthValidator(11)],
        help_text="Digite o CPF",
        verbose_name="CPF",
    )
    def __str__(self):
        return self.name