"""ParkingManagment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from core import views as core_views
from sucursales import views as sucursales_views
from django.urls import path,include
from rest_framework.authtoken import views

urlpatterns = [
    #path('', core_views.home, name='home'),
    path('sucursales/', sucursales_views.sucursales, name='sucursales'),
    path('about-me/', core_views.about, name='about-me'),
    path('contact/', core_views.contact, name='contact'),
    path('', include('admin_app.urls')),
    path('', include('demo_app.urls_1_8')),
    path('api/cortes/', include('admin_app.api.urls'), name = 'cortes-api'),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('api/auth', include('rest_framework.urls'), name='rest_framework'),
]
