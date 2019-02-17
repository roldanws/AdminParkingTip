from django.contrib import admin

# Register your models here.
from .models import Suscripcion
# Register your models here.

class suscripcionAdmin(admin.ModelAdmin):
    readonly_fields = ('updated',)


admin.site.register(Suscripcion,suscripcionAdmin)
