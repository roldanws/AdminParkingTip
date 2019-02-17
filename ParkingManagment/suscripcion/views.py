from django.shortcuts import render,get_object_or_404
from .models import Suscripcion
from admin_app.models import Sucursal
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.


@method_decorator(login_required, name="dispatch")
class SuscripcionListView(ListView):
    model = Suscripcion
    paginate_by = 12
    def get_queryset(self):
        #context['temp'] = self.request.GET.get('temp') 
        
        self.sucursal_id = get_object_or_404(Sucursal, id=self.kwargs['sucursal_id'])
        suscripcion = Suscripcion.objects.filter(sucursal_id=self.sucursal_id)
        query = self.request.GET.get('s')  
        if query:
            suscripcion = suscripcion.filter(nombre__icontains=query)
        return suscripcion


class SuscripcionDetailView(DetailView):
    model = Suscripcion