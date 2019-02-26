from django.db import models
from django.utils.timezone import now
from admin_app.models import Sucursal
# Create your models here.


class Suscripcion(models.Model):
    nombre = models.CharField(max_length=200, verbose_name = 'Nombre')
    apellidos = models.CharField(max_length=200, verbose_name = 'Apellidos', default="-")
    TURNOS = (
        ("Matutino", "Matutino"),
        ("Nocturno", "Nocturno"),
        ("Completo", "Completo"),
    )
    TIPO = (
        ("Locatario", "Locatario"),
        ("Pensionado", "Pensionado"),
        ("Otro", "Otro"),
    )
    turno = models.CharField(max_length=50, choices=TURNOS, verbose_name = 'Turno')
    tipo = models.CharField(max_length=50, choices=TIPO, verbose_name = 'tipo',default='Locatario')
    clave =  models.CharField(max_length=50, verbose_name = 'ID')
    activo =  models.BooleanField(verbose_name = 'Activo')
    created = models.DateTimeField(verbose_name = 'Fecha de pago', default = now)
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Ultimo Pago')
    costo = models.DecimalField(verbose_name='Costo', max_digits=15, decimal_places=2)
    sucursal_id = models.ForeignKey(Sucursal, verbose_name = 'Sucursal', related_name='get_suscripcion', on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Suscripcion'
        verbose_name_plural = 'Suscripcion'
        ordering = ['-id']

    def __str__(self):
        return str(self.nombre)