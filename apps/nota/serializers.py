from rest_framework import serializers

from apps.nota.models import *

class EtiquetaSerializers(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Etiqueta
        fields = ('id', 'nombre')
