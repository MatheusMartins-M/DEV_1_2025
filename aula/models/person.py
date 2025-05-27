from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from aula.models.base_model import BaseModel
from ..managers.exemplo import ExemploManager

class Person(BaseModel):
    name = models.CharField(
        null=False, blank=False,
        max_length=100,
        help_text="Digite o nome",
        verbose_name="Nome",
    )
    birth_date= models.DateField(
        null=False, blank=False,
        default='',
        help_text="Digite a data",
        verbose_name="Data de aniversário"
    )
    cpf = models.CharField(
        null=False, blank=False,
        max_length=11,
        validators=[MinLengthValidator(11), MaxLengthValidator(11)],
        help_text= "Digite o CPF",
        verbose_name= "CPF",
    )

    objects = ExemploManager()

    def __str__(self):
        return self.name