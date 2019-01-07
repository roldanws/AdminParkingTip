from django.contrib import admin
from .models import Sucursal,Corte
# Register your models here.

class sucursalAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class corteAdmin(admin.ModelAdmin):
    readonly_fields = ('updated',)




admin.site.register(Sucursal,sucursalAdmin)
admin.site.register(Corte,corteAdmin)

