from django.db import models
from aula.models.base_model import BaseModel
from .magazine import Magazine
from .article import Article
from .person import Person

class Publication(BaseModel):
    magazine = models.ForeignKey(Magazine, on_delete=models.RESTRICT)
    article = models.ForeignKey(Article, on_delete=models.RESTRICT)
    editor = models.ForeignKey(Person, on_delete=models.RESTRICT)
    date = models.DateField()
    obs = models.TextField()