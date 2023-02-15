from rest_framework import serializers
from modelo_datos.models import Punto

class puntoSerializer(serializers.Serializer):
    
    id = serializers.IntegerField(read_only=True)
    nombre_punto = serializers.CharField()
    longitud = serializers.FloatField()
    latitud = serializers.FloatField()
    