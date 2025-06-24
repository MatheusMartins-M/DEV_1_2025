from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from services.serializers import UserSerializer
from django.contrib.auth.models import User

from services.views.base_security import BaseSecurity


class UserViewSet(BaseSecurity, ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    @action(methods=['get'], detail=False)
    def mensagem(self, request, format=None):
        return Response({"mensagem": f"Olá Mundo, {request.data}", })