from admin_app.models import Corte
from rest_framework.serializers import ModelSerializer


class CorteListSerializer(ModelSerializer):
    class Meta:
        model = Corte
        fields = ['turno','boletaje','recuperados','caja','created','updated','ingreso','encargado','sucursal_id']
        
class CorteDetailSerializer(ModelSerializer):
    class Meta:
        model = Corte
        fields = ['turno','boletaje','recuperados','caja','created','updated','ingreso','encargado','sucursal_id']
        
class CorteCreateSerializer(ModelSerializer):
    class Meta:
        model = Corte
        fields = ['turno','boletaje','recuperados','caja','created','updated','ingreso','encargado','sucursal_id']
        

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