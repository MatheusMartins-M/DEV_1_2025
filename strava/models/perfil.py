from strava.models.base_model import BaseModel
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
from strava.enumerations.genero import Genero

class Perfil(BaseModel):
    email = models.EmailField(
        null=False, blank=False, unique=True,
        validators=[MinLengthValidator(10), MaxLengthValidator(100)],
        help_text="Digite o seu email",
        verbose_name="E-mail",
    )
    nome = models.CharField(
        max_length=200, null=False, blank=False,
        validators=[MinLengthValidator(10), MaxLengthValidator(100)],
        help_text="Digite o seu nome",
        verbose_name="Nome",
    )
    cpf = models.CharField(
        null=False, blank=False, unique=True,
        max_length=11,
        validators=[MinLengthValidator(11), MaxLengthValidator(11)],
        help_text="Digite o seu CPF",
        verbose_name="CPF",
    )
    senha = models.CharField(
        null=False, blank=False,
        max_length=20,
        validators=[MinLengthValidator(5), MaxLengthValidator(20)],
        help_text="Digite sua senha",
        verbose_name="Senha",
    )
    data_nascimento = models.DateField(
        null=False, blank=False,
        help_text = "Digite data de nascimento",
        verbose_name = "Data de nascimento"
    )
    local = models.CharField(
        null=False, blank=False,
        max_length=100,
        validators=[MinLengthValidator(3), MaxLengthValidator(100)],
        help_text="Digite o seu local",
        verbose_name="Local",
    )
    pais = models.CharField(
        null=False, blank=False,
        max_length=100,
        validators=[MinLengthValidator(3), MaxLengthValidator(100)],
        help_text="Digite o seu país",
        verbose_name="País",
    )
    genero = models.CharField(
        max_length=5, null=False, blank=False,
        choices=Genero, default=Genero.NOT_INFORMED,
        help_text="Selecione o genero",
        verbose_name="Gênero",
    )
    peso = models.FloatField(
        validators=[MinValueValidator(20)],
        default=0.00, null=True, blank=True,
        help_text="Digite seu peso",
        verbose_name="Peso",
    )
    pagina_pessoal = models.URLField(
        null=False, blank=False,
        validators=[MinLengthValidator(15), MaxLengthValidator(150)],
        help_text="Digite a URL da sua pagina",
        verbose_name="URL",
    )
    biografia = models.TextField(
        null=True, blank=True,
        help_text="Digite sua biografia (opcional)",
        verbose_name="Biografia",
    )
    premium = models.BooleanField(
        default=False, null=False, blank=False,
        help_text="É premium?",
        verbose_name="Premium",
    )
    membro_desde = models.DateField(
        null=False, blank=False,
        auto_now_add=True,
        help_text="Digite a data",
        verbose_name="Data de quando começou"
    )

    def __str__(self):
        return self.nome