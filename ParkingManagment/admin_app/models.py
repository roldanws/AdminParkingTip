from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Sucursal(models.Model):
    nombre = models.CharField(max_length=200, verbose_name = 'Sucursal')
    localidad = models.CharField(max_length=200, verbose_name = 'Estado')
    telefono = models.CharField(max_length=200, verbose_name = 'Telefono')
    #tipo = models.PositiveSmallIntegerField(verbose_name = 'Tipo')
    #cobro = models.PositiveSmallIntegerField(verbose_name = 'Esquema')
    entradas = models.PositiveSmallIntegerField(verbose_name = 'Entradas')
    salidas = models.PositiveSmallIntegerField(verbose_name = 'Salidas')
    #ingreso_actual = models.PositiveIntegerField(verbose_name = 'Ingresos')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de ultima modificacion')
    class Meta:
        verbose_name = 'sucursal'
        verbose_name_plural = 'sucursales'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Corte(models.Model):
    TURNOS = (
        ("Matutino", "Matutino"),
        ("Vespertino", "Vespertino"),
        ("Nocturno", "Nocturno"),
    )
    turno = models.CharField(max_length=50, choices=TURNOS, verbose_name = 'Turno')
    boletaje =  models.PositiveSmallIntegerField(verbose_name = 'Boletos Expedidos')
    recuperados = models.PositiveIntegerField(verbose_name = 'Recuperados')
    caja = models.PositiveSmallIntegerField(verbose_name = 'Caja')
    created = models.DateTimeField(verbose_name = 'Fecha de corte', default = now)
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de ultima modificacion')
    ingreso = models.DecimalField(verbose_name='Ingreso', max_digits=15, decimal_places=2)
    detalles = models.TextField(verbose_name='Detalles')
    encargado = models.ForeignKey(User, verbose_name = 'Encargado', on_delete = models.CASCADE)
    sucursal_id = models.ForeignKey(Sucursal, verbose_name = 'Sucursal', related_name='get_cortes', on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Corte'
        verbose_name_plural = 'Cortes'
        ordering = ['-created']

    def __str__(self):
        return str(self.created)+' '+self.turno