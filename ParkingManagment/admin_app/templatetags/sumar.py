from django import template
from admin_app.models import Corte,Sucursal
from django.db.models import Sum, Q


register = template.Library()

@register.simple_tag
def sumar(corte):
    resultado=int(corte.boletaje)-int(corte.recuperados)-int(corte.tolerancias)-int(corte.locatarios)
    return resultado
