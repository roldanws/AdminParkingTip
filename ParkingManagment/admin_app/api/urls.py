from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from .views import CorteListApiView, CorteDetailApiView, CorteCreateApiView

app_name = 'admin_app'
urlpatterns = [
    path('', CorteListApiView.as_view(), name='list'), 
    #path('(?P<pk>\d+)/', CorteDetailApiView.as_view(), name='detail'),   
    url(r'^(?P<pk>\d+)/$', CorteDetailApiView.as_view(), name='detail'),
    url(r'^create/$', CorteCreateApiView.as_view(), name='create'),
    #path('', SucursalListView.as_view(), name='sucursal'),
]