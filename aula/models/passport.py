from django.db import models
from aula.models import Person
from aula.models.base_model import BaseModel
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Passport(BaseModel):
    number = models.CharField(
        null=False, blank=False,
        max_length=8,
        validators=[MinLengthValidator(8), MaxLengthValidator(8)],
        help_text="Digite os dígitos do passaporte",
        verbose_name=" Dígitos do Passaporte",
    )
    issue_date = models.DateField(
        null=False, blank=False,
        default='',
        help_text="Digite a data",
        verbose_name="Data de Expedição"
    )
    expiration_date = models.DateField(
        null=False, blank=False,
        default='',
        help_text="Digite a data",
        verbose_name="Data de Expiração"
    )
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    def __str__(self):
        return f'{self.person.name} - {self.number}'