from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from services.views import *
from rest_framework import routers

app_name = 'services'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', api_root, name="api-root"),
    path('saudacao', saudacao, name="saudacao"),
    path('calculo', calculo, name="calculo"),
    path('auth', obtain_auth_token)
]

urlpatterns += router.urls