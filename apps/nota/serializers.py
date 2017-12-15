from rest_framework import serializers

from apps.nota.models import *

class EtiquetaSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Etiqueta
        fields = ('id', 'nombre')

class EtiquetaIDSerializer(serializers.ModelSerializer):
    tag_ids = serializers.ListField(child=serializers.IntegerField())

class NotaSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    
    class Meta:
        model = Nota
        fields = ('id', 'titulo', 'contenido', 'fecha')

class NotaEtiquetaSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    etiqueta = EtiquetaSerializer(read_only=True)
    nota = NotaSerializer(read_only=True)

    class Meta:
        model = NotaEtiqueta
        fields = ('id', 'etiqueta', 'nota')
