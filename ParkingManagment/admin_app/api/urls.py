from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from .views import CorteListApiView, CorteDetailApiView, CorteCreateApiView, SuscripcionListApiView, SuscripcionDetailApiView, SuscripcionCreateApiView

app_name = 'admin_app'
urlpatterns = [
    path('cortes/', CorteListApiView.as_view(), name='list'), 
    #path('(?P<pk>\d+)/', CorteDetailApiView.as_view(), name='detail'),   
    path('cortes/<int:pk>/', CorteDetailApiView.as_view(), name='detail'),
    path('cortes/create/', CorteCreateApiView.as_view(), name='create'), 

    path('suscripciones/<int:sucursal_id>/', SuscripcionListApiView.as_view(), name='list'), 
    #path('(?P<pk>\d+)/', CorteDetailApiView.as_view(), name='detail'),   
    path('suscripcion/<int:pk>/', SuscripcionDetailApiView.as_view(), name='detail'),
    path('suscripcion/create/', SuscripcionCreateApiView.as_view(), name='create'),
]