from django.db import models
from aula.models.magazine import Magazine
from aula.models.reporter import Reporter
from aula.models.base_model import BaseModel

class Article(BaseModel):
    name = models.CharField(
        null=False, blank=False,
        max_length=100,
        help_text="Digite o nome",
        verbose_name="Nome",
    )
    pub_date = models.DateField(
        null=False, blank=False,
        default='Digite a data',
        help_text="Digite a data",
        verbose_name="Data da publicação"
    )
    reporter = models.ForeignKey(
        Reporter,
        on_delete=models.CASCADE,
    )
    magazines = models.ManyToManyField(
        Magazine, null=True, blank=True,
        through="Publication",
        through_fields=("article", "magazine")
    )

    def __str__(self):
        return f'{self.name} by {self.reporter.name}'