from django.shortcuts import render,get_object_or_404
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView
from admin_app.models import Corte, Excepcion, Sucursal
from suscripcion.models import Suscripcion
from .serializers import CorteListSerializer,CorteDetailSerializer,CorteCreateSerializer , SuscripcionListSerializer,SuscripcionDetailSerializer, SuscripcionCreateSerializer



class CorteListApiView(ListAPIView):
    queryset = Corte.objects.all()
    serializer_class = CorteListSerializer
    '''def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset, 
            pk=self.kwargs['pk'],
        )
        return obj'''

class CorteDetailApiView(RetrieveAPIView):
    queryset = Corte.objects.all()
    serializer_class = CorteDetailSerializer

class CorteCreateApiView(CreateAPIView):
    queryset = Corte.objects.all()
    serializer_class = CorteCreateSerializer



class SuscripcionListApiView(ListAPIView):
    serializer_class = SuscripcionListSerializer
    def get_queryset(self):
        self.sucursal_id = get_object_or_404(Sucursal, id=self.kwargs['sucursal_id'])
        suscripciones = Suscripcion.objects.filter(sucursal_id=self.sucursal_id)
        clave = self.request.GET.get('clave', None)
        print(self.sucursal_id)
        if clave is not None:
            suscripciones = suscripciones.filter(clave=clave)
        return suscripciones

    

class SuscripcionDetailApiView(RetrieveAPIView):
    queryset = Suscripcion.objects.all()
    serializer_class = SuscripcionDetailSerializer

class SuscripcionCreateApiView(CreateAPIView):
    queryset = Suscripcion.objects.all()
    serializer_class =  SuscripcionCreateSerializer
