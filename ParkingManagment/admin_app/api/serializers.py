from admin_app.models import Corte
from suscripcion.models import Suscripcion
from rest_framework.serializers import ModelSerializer


class CorteListSerializer(ModelSerializer):
    class Meta:
        model = Corte
        fields = ['turno','boletaje','recuperados','sellados','noSellados','incompletos','propina','sinPropina','tolerancias','locatarios','cortesias','caja','created','updated','ingreso','detalles','encargado','sucursal_id']
        
class CorteDetailSerializer(ModelSerializer):
    class Meta:
        model = Corte
        fields = ['turno','boletaje','recuperados','sellados','noSellados','incompletos','propina','sinPropina','tolerancias','locatarios','cortesias','caja','created','updated','ingreso','detalles','encargado','sucursal_id']
        
class CorteCreateSerializer(ModelSerializer):
    class Meta:
        model = Corte
        fields = ['turno','boletaje','recuperados','sellados','noSellados','incompletos','propina','sinPropina','tolerancias','locatarios','cortesias','caja','created','updated','ingreso','detalles','encargado','sucursal_id']
        


class SuscripcionListSerializer(ModelSerializer):
    class Meta:
        model = Suscripcion
        fields = ['nombre','apellidos','turno','tipo','clave','activo','created','updated','costo','sucursal_id']
        
class SuscripcionDetailSerializer(ModelSerializer):
    class Meta:
        model = Suscripcion
        fields = ['nombre','apellidos','turno','tipo','clave','activo','created','updated','costo','sucursal_id']
        
class SuscripcionCreateSerializer(ModelSerializer):
    class Meta:
        model = Suscripcion
        fields = ['nombre','apellidos','turno','tipo','clave','activo','created','updated','costo','sucursal_id']
        



  


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