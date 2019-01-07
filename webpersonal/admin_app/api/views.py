from django.shortcuts import render,get_object_or_404
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView
from admin_app.models import Corte
from .serializers import CorteListSerializer,CorteDetailSerializer,CorteCreateSerializer



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
