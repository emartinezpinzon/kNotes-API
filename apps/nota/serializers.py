from rest_framework import serializers

from apps.nota.models import *

class EtiquetaSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Etiqueta
        fields = ('id', 'nombre')
