from django.shortcuts import render,get_object_or_404
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView
from admin_app.models import Corte, Excepcion, Sucursal
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
    serializer_class = ExcepcionListSerializer
    def get_queryset(self):
        self.sucursal_id = get_object_or_404(Sucursal, id=self.kwargs['sucursal_id'])
        excepciones = Excepcion.objects.filter(sucursal_id=self.sucursal_id)
        folio = self.request.GET.get('folio', None)
        print(self.sucursal_id)
        if folio is not None:
            excepciones = excepciones.filter(folio=folio)
        return excepciones

    

class ExcepcionDetailApiView(RetrieveAPIView):
    queryset = Excepcion.objects.all()
    serializer_class = ExcepcionDetailSerializer

class ExcepcionCreateApiView(CreateAPIView):
    queryset = Excepcion.objects.all()
    serializer_class =  ExcepcionCreateSerializer
