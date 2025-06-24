from django.db import models
from rest_framework import serializers

class OperacoesNoCalculo(models.TextChoices):
    ADDITION = "+", "Adição"
    SUBTRACTION = "-", "Subtração"
    MULTIPLICATION = "*", "Multiplicação"
    DIVISION = "/", "Divisão"

class CalculoSerializer(serializers.Serializer):
    primeiro_termo = serializers.FloatField(required=True)
    segundo_termo = serializers.FloatField(required=True)
    operacao = serializers.ChoiceField(required=True, choices=OperacoesNoCalculo.choices)
    resultado = serializers.CharField(required=False)

    class Meta:
        fields = ['primeiro_termo', 'segundo_termo', 'operacao']

    def calcular(self):
        primeiro_termo = self.validated_data.get('primeiro_termo')
        segundo_termo = self.validated_data.get('segundo_termo')
        operacao = self.validated_data.get('operacao')

        match operacao:
            case OperacoesNoCalculo.ADDITION:
                self.validated_data.update({'resultado': primeiro_termo + segundo_termo})
                self.validated_data.update({'operacao': OperacoesNoCalculo.ADDITION.label})

            case OperacoesNoCalculo.SUBTRACTION:
                self.validated_data.update({'resultado': primeiro_termo - segundo_termo})
                self.validated_data.update({'operacao': OperacoesNoCalculo.SUBTRACTION.label})

            case OperacoesNoCalculo.MULTIPLICATION:
                self.validated_data.update({'resultado': primeiro_termo * segundo_termo})
                self.validated_data.update({'operacao': OperacoesNoCalculo.MULTIPLICATION.label})

            case OperacoesNoCalculo.DIVISION:
                if segundo_termo == 0:
                    self.validated_data.update({'resultado': 0})
                else:
                    self.validated_data.update({'resultado': primeiro_termo / segundo_termo})
                self.validated_data.update({'operacao': OperacoesNoCalculo.DIVISION.label})

            case _:
                raise NotImplementedError("Not Implemented")