from aula.forms import BaseForm
from aula.models.exemplo import Exemplo

class ExemploForm(BaseForm):
    class Meta:
        model = Exemplo
        fields = '__all__'