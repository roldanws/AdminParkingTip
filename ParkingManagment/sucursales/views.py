from django.shortcuts import render
#from .models import Sucursal

# Create your views here.

def sucursales(request):  
#    sucursales = Sucursal.objects.all()
    return render(request,'sucursales/sucursales.html', {'sucursales':sucursales})

