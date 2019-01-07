from admin_app.models import Corte
from rest_framework import serializers

class CorteSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="cortes:sucursal_id",
        lookup_field = 'sucursal_id'
        )
    class Meta:
        model = Corte
        fields = ('url','turno','boletaje','recuperados','caja','created','updated','ingreso')
        #fields = ('turno','boletaje','recuperados','caja','created','updated','ingreso')
        