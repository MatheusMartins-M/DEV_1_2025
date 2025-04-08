from django.core.validators import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_par(valor):
    if int(valor) % 2 != 0:
        raise ValidationError(
            _("Não é um número par"),
            params={"valor": valor}
        )