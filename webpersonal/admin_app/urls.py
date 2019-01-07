from django.urls import path
from . import views
from .views import SucursalDetailView,CorteListView


app_name = 'admin_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('tables', views.tables, name='tables'),
    path('flot', views.flot, name='flot'),
    path('morris', views.morris, name='morris'),
    path('forms', views.forms, name='forms'),
    path('panels_wells', views.panels_wells, name='panels_wells'),
    path('buttons', views.buttons, name='buttons'),
    path('notifications', views.notifications, name='notifications'),
    path('typography', views.typography, name='typography'),
    path('icons', views.icons, name='icons'),
    path('grid', views.grid, name='grid'),
    path('blank', views.blank, name='blank'),
    path('login', views.login, name='login'),
    path('sucursal/<int:pk>/', SucursalDetailView.as_view(), name='sucursal'),
    path('cortes/<int:sucursal_id>/', CorteListView.as_view(), name='corte'),    
    #path('', SucursalListView.as_view(), name='sucursal'),
]