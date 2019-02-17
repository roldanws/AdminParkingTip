from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from .views import CorteListApiView, CorteDetailApiView, CorteCreateApiView, ExcepcionListApiView, ExcepcionDetailApiView, ExcepcionCreateApiView

app_name = 'admin_app'
urlpatterns = [
    path('cortes/', CorteListApiView.as_view(), name='list'), 
    #path('(?P<pk>\d+)/', CorteDetailApiView.as_view(), name='detail'),   
    path('cortes/<int:pk>/', CorteDetailApiView.as_view(), name='detail'),
    path('cortes/create/', CorteCreateApiView.as_view(), name='create'), 

    path('excepciones/<int:sucursal_id>/', ExcepcionListApiView.as_view(), name='list'), 
    #path('(?P<pk>\d+)/', CorteDetailApiView.as_view(), name='detail'),   
    path('excepciones/<int:pk>/', ExcepcionDetailApiView.as_view(), name='detail'),
    path('excepciones/create/', ExcepcionCreateApiView.as_view(), name='create'),
]