from django.urls import path
from .views import SuscripcionDetailView,SuscripcionListView

suscripcion_patterns = ([
    path('suscripciones/<int:sucursal_id>/', SuscripcionListView.as_view(), name="list"),
    path('suscripcion/<int:pk>/', SuscripcionDetailView.as_view(), name="detail")
],"suscripcion")
