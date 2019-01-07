from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from .serializers import CorteSerializer
from admin_app.models import Corte
# Create your views here.

class CorteApiList(generics.ListCreateAPIView):
    queryset = Corte.objects.all()
    serializer_class = CorteSerializer
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset, 
            pk=self.kwargs['pk'],
        )
        return obj
