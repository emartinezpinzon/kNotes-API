from rest_framework import serializers

from apps.nota.models import *

class EtiquetaSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Etiqueta
        fields = ('id', 'nombre')

class NotaSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    etiqueta = EtiquetaSerializer(read_only=True)
    
    class Meta:
        model = Nota
        fields = ('id', 'titulo', 'contenido', 'etiqueta', 'fecha')
