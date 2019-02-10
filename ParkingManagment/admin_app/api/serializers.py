from admin_app.models import Corte,Excepcion
from rest_framework.serializers import ModelSerializer


class CorteListSerializer(ModelSerializer):
    class Meta:
        model = Corte
        fields = ['turno','boletaje','recuperados','tolerancias','locatarios','caja','created','updated','ingreso','detalles','encargado','sucursal_id']
        
class CorteDetailSerializer(ModelSerializer):
    class Meta:
        model = Corte
        fields = ['turno','boletaje','recuperados','tolerancias','locatarios','caja','created','updated','ingreso','detalles','encargado','sucursal_id']
        
class CorteCreateSerializer(ModelSerializer):
    class Meta:
        model = Corte
        fields = ['turno','boletaje','recuperados','tolerancias','locatarios','caja','created','updated','ingreso','detalles','encargado','sucursal_id']
        


class ExcepcionListSerializer(ModelSerializer):
    class Meta:
        model = Excepcion
        fields = ['nombre','turno','folio','activo','created','updated','costo','sucursal_id']
        
class ExcepcionDetailSerializer(ModelSerializer):
    class Meta:
        model = Excepcion
        fields = ['nombre','turno','folio','activo','created','updated','costo','sucursal_id']
        
class ExcepcionCreateSerializer(ModelSerializer):
    class Meta:
        model = Excepcion
        fields = ['nombre','turno','folio','activo','created','updated','costo','sucursal_id']
        



  


'''
{
    "turno": 'Matutino',
    "boletaje": 22,
    "recuperados": 22,
    "caja": 2,
    "created": '2018-12-12T12:12',
    "ingreso": 122,
    "encargado": 'eum',
    "sucursal_id": 4
}
'''