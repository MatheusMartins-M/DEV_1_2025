from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.reverse import reverse

from services.serializers import CalculoSerializer


@api_view(['GET'])
def saudacao(request):
    return Response({"saudacao": "Olá Mundo"})

@api_view(['GET', 'POST'])
def calculo(request):
    try:
        if request.method == 'GET':
            serializer = CalculoSerializer()
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            dados = JSONParser().parse(request)
            serializer = CalculoSerializer(data=dados)
            if serializer.is_valid():
                serializer.calcular()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        context = {
            "error": str(e)
        }
        return JsonResponse(context, status=status.HTTP_400_BAD_REQUEST, safe=False)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'saudacao': reverse('services:saudacao', request=request, format=format),
        'calculo': reverse('services:calculo', request=request, format=format),
        'users': reverse('services:user-list', request=request, format=format),
    })