"""
URL configuration for DEV_1_2025 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls.conf import include
from DEV_1_2025.views import index, ContactView
from DEV_1_2025.views.search import SearchView
from DEV_1_2025.forms import CustomLoginForm

urlpatterns = [
    path('', index, name="index"),
    path('sistema', index, name="index"),
    path('admin/', admin.site.urls),
    path('aula/', include('aula.urls')),
    path('search/', SearchView.as_view(), name="Search"),
    #path('function/contato/', contact, name='function_contact'),
    path('classe/contato/', ContactView.as_view(), name='class_contact'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name="accounts/login.html", authentication_form=CustomLoginForm)),
    path('accounts/', include('django.contrib.auth.urls')),

    path('services/', include('services.urls')),
]
