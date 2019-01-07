from django.shortcuts import render,get_object_or_404
from .models import Sucursal,Corte
from django.db.models import Sum
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from rest_framework import generics
#from .serializers import CorteSerializer


def index(request):
    
    sucursales = Sucursal.objects.all()
    suma = []
    total=0
    for sucursal in sucursales:
        suma_parcial=Sucursal.objects.get(id=sucursal.id).get_cortes.all().aggregate(Sum('ingreso'))['ingreso__sum']
        suma.append(suma_parcial)
        total=total+suma_parcial
    #suma = Sucursal.objects.filter(nombre__contains='oln').aggregate(Sum('ingreso_actual'))
    
    suma=suma[::-1]
    print(suma[::-1])
    return render(request, 'admin_app/dashboard.html', {'sucursales':sucursales,'suma':suma,'total':total} )

'''class CorteApiList(generics.ListCreateAPIView):
    queryset = Corte.objects.all()
    serializer_class = CorteSerializer
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset, 
            pk=self.kwargs['pk'],
        )
        return obj'''



class CorteListView(ListView):
    model = Corte

    def get_queryset(self):
        self.sucursal_id = get_object_or_404(Sucursal, id=self.kwargs['sucursal_id'])
        return Corte.objects.filter(sucursal_id=self.sucursal_id)
    #sucursal = Sucursal.objects.get(id=sucursal_id)
    #return render(request, 'admin_app/page_details.html',{'sucursal':sucursal})


class SucursalDetailView(DetailView):
    model = Sucursal
    #sucursal = Sucursal.objects.get(id=sucursal_id)
    #return render(request, 'admin_app/page_details.html',{'sucursal':sucursal})
    

def tables(request):
    return render(request, 'admin_app/tables.html')

def flot(request):
    return render(request, 'admin_app/flot.html')

def morris(request):
    return render(request, 'admin_app/morris.html')

def forms(request):
    return render(request, 'admin_app/forms.html')

def panels_wells(request):
    return render(request, 'admin_app/panels_wells.html')

def buttons(request):
    return render(request, 'admin_app/buttons.html')

def notifications(request):
    return render(request, 'admin_app/notifications.html')

def typography(request):
    return render(request, 'admin_app/typography.html')

def icons(request):
    return render(request, 'admin_app/icons.html') 

def grid(request):
    return render(request, 'admin_app/grid.html')   

def blank(request):
    return render(request, 'admin_app/blank.html')

def login(request):
    return render(request, 'admin_app/login.html')                     
