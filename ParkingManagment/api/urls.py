from django.urls import path
from . import views
from .views import CorteApiList

app_name = 'admin_app'
urlpatterns = [
    path('cortes/', CorteApiList.as_view(), name = 'cortes'),
]