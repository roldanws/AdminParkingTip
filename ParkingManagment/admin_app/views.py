from django.shortcuts import render,get_object_or_404
from .models import Sucursal,Corte
from django.db.models import Sum
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from rest_framework import generics

class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
    
@method_decorator(staff_member_required, name="dispatch")
class SucursalListView(ListView):
    model = Sucursal
    def get_queryset(self):
        sucursales = Sucursal.objects.all()
        query = self.request.GET.get('s')  
        if query:
            sucursales = sucursales.filter(nombre__icontains=query)
        return sucursales

    def get_context_data(self, **kwargs):
        sucursales = Sucursal.objects.all()
        suma = []
        total=0
        query = self.request.GET.get('s')  
        if query:
            sucursales = sucursales.filter(nombre__icontains=query)
        for sucursal in sucursales:
            suma_parcial=Sucursal.objects.get(id=sucursal.id).get_cortes.all().aggregate(Sum('ingreso'))['ingreso__sum']
            suma.append(suma_parcial)
            total=total+suma_parcial
        #suma = Sucursal.objects.filter(nombre__contains='oln').aggregate(Sum('ingreso_actual'))
        suma=suma[::-1]
        print(suma[::-1])

        
        context = super().get_context_data(**kwargs)
        context['suma']=suma
        context['total']=total
        return context


@method_decorator(staff_member_required, name="dispatch")
class CorteListView(ListView):
    model = Corte
    def get_queryset(self):
        #context['temp'] = self.request.GET.get('temp') 

        self.sucursal_id = get_object_or_404(Sucursal, id=self.kwargs['sucursal_id'])
        cortes = Corte.objects.filter(sucursal_id=self.sucursal_id)
        query = self.request.GET.get('q') 
        query2 = self.request.GET.get('q2') 
        #mes = self.request.GET.get('mes') 
        #anio = self.request.GET.get('anio') 
        if query:
            cortes = cortes.filter(created__range=[query, query2])
            
        return cortes

@method_decorator(staff_member_required, name="dispatch")
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
