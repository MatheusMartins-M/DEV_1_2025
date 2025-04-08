import random
import string

from django.core.validators import MinLengthValidator
from django.db import models
from .person import Person
from aula.models.base_model import BaseModel
from aula.validators import CodValidator
from aula.validators import validate_par
from rest_framework.exceptions import ValidationError
#from ..managers.exemplo import ExemploManager

class Exemplo(BaseModel):

    cod = models.CharField(
        blank=True, max_length=10,
        validators=[MinLengthValidator(10),
                    CodValidator("4444444444"),
                    validate_par]
    )
    nome = models.CharField(max_length=15, validators=[MinLengthValidator(3)])
    people = models.ManyToManyField(Person, blank=True, null=True)

    #objects = ExemploManager()

    def __str__(self):
        return self.nome

    #qualquer coisa que eu queria alterar nos dados antes de salvar
    def save(self, *args, **kargs):
        if self.cod is None or self.cod == '':
            letters = string.ascii_letters + string.digits
            self.cod = ''.join(random.choice(letters) for i in range(10))
        super().save(*args, **kargs)

    def clean(self):
        if not isinstance(str(self.nome), str):
            raise ValidationError({
                "nome": 'Nome informado é do tipo errado'},
                code='error001')
        elif self.nome == "Teste":
            raise ValidationError(
                {"nome": 'Não é possível salvar testes!'},
                code="error002")
        elif self.cod == "1111111111" and self.nome == "IFRS Restinga":
            raise ValidationError(
                {"nome": 'Combinação de nome e código errada!',
                 "cod": 'Combinação de nome e código errada!'},
                code="erro0101")