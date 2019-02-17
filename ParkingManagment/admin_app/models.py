from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Sucursal(models.Model):
    TIPOS = (
        ("Automatizado", "Automatizado"),
        ("Semi-automatizado", "Semi-automatizado"),
        ("Aportacion", "Aportacion"),
    )
    nombre = models.CharField(max_length=200, verbose_name = 'Sucursal')
    tipo = models.CharField(max_length=200, choices= TIPOS, verbose_name = 'Tipo' ,default="Automatizado")
    localidad = models.CharField(max_length=200, verbose_name = 'Estado')
    telefono = models.CharField(max_length=200, verbose_name = 'Telefono')
    #tipo = models.PositiveSmallIntegerField(verbose_name = 'Tipo')
    #cobro = models.PositiveSmallIntegerField(verbose_name = 'Esquema')
    entradas = models.PositiveSmallIntegerField(verbose_name = 'Entradas')
    salidas = models.PositiveSmallIntegerField(verbose_name = 'Salidas')
    #ingreso_actual = models.PositiveIntegerField(verbose_name = 'Ingresos')
    supervisor = models.ForeignKey(User, verbose_name = 'Supervisor', on_delete = models.CASCADE, default='1')
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
    sellados = models.PositiveIntegerField(verbose_name = 'Sellados', blank="True", default=0)
    noSellados = models.PositiveIntegerField(verbose_name = 'No sellados', blank="True", default=0)
    incompletos = models.PositiveIntegerField(verbose_name = 'Incompletos', blank="True", default=0)
    propina = models.PositiveIntegerField(verbose_name = 'Propina', blank="True", default=0)
    sinPropina = models.PositiveIntegerField(verbose_name = 'Sin propina', blank="True", default=0)
    tolerancias =  models.PositiveIntegerField(verbose_name = 'Tolerancias', blank="True", default=0)
    locatarios = models.PositiveIntegerField(verbose_name = 'Locales', blank="True", default=0)
    cortesias = models.PositiveIntegerField(verbose_name = 'Cortesias', blank="True", default=0)
    caja = models.PositiveSmallIntegerField(verbose_name = 'Caja')
    ingreso = models.DecimalField(verbose_name='Ingreso', max_digits=15, decimal_places=2)
    detalles = models.TextField(verbose_name='Detalles')
    encargado = models.ForeignKey(User, verbose_name = 'Encargado', on_delete = models.CASCADE)
    sucursal_id = models.ForeignKey(Sucursal, verbose_name = 'Sucursal', related_name='get_cortes', on_delete = models.CASCADE)
    created = models.DateTimeField(verbose_name = 'Fecha de corte', default = now)
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de ultima modificacion')

    class Meta:
        verbose_name = 'Corte'
        verbose_name_plural = 'Cortes'
        ordering = ['-created']

    def __str__(self):
        return str(self.created)+' '+self.turno




class Excepcion(models.Model):
    nombre = models.CharField(max_length=200, verbose_name = 'Nombre')
    TURNOS = (
        ("Matutino", "Matutino"),
        ("Nocturno", "Nocturno"),
        ("Completo", "Completo"),
    )
    turno = models.CharField(max_length=50, choices=TURNOS, verbose_name = 'Turno')
    folio =  models.PositiveSmallIntegerField(verbose_name = 'Folio')
    activo =  models.BooleanField(verbose_name = 'Activo')
    created = models.DateTimeField(verbose_name = 'Fecha de pago', default = now)
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Ultimo Pago')
    costo = models.DecimalField(verbose_name='Costo', max_digits=15, decimal_places=2)
    sucursal_id = models.ForeignKey(Sucursal, verbose_name = 'Sucursal', related_name='get_excepcion', on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Excepcion'
        verbose_name_plural = 'Excepciones'
        ordering = ['-folio']

    def __str__(self):
        return str(self.nombre)