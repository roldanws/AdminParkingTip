from django.shortcuts import render,get_object_or_404
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView
from admin_app.models import Corte, Excepcion
from .serializers import CorteListSerializer,CorteDetailSerializer,CorteCreateSerializer , ExcepcionListSerializer, ExcepcionDetailSerializer, ExcepcionCreateSerializer



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



class  ExcepcionListApiView(ListAPIView):
    queryset = Excepcion.objects.all()
    serializer_class = ExcepcionListSerializer

class ExcepcionDetailApiView(RetrieveAPIView):
    queryset = Excepcion.objects.all()
    serializer_class = ExcepcionDetailSerializer

class ExcepcionCreateApiView(CreateAPIView):
    queryset = Excepcion.objects.all()
    serializer_class =  ExcepcionCreateSerializer
