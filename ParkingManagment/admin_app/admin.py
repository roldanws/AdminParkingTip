from django.contrib import admin
from .models import Sucursal,Corte, Excepcion
# Register your models here.

class sucursalAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class corteAdmin(admin.ModelAdmin):
    readonly_fields = ('updated',)

class exceptionAdmin(admin.ModelAdmin):
    readonly_fields = ('updated',)




admin.site.register(Sucursal,sucursalAdmin)
admin.site.register(Corte,corteAdmin)
admin.site.register(Excepcion,exceptionAdmin)

