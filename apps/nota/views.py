from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from apps.nota.models import *
from apps.nota.serializers import *

class EtiquetaList(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes=(IsAuthenticated, )
    
    def post(self, request, format=None):
        nombre = request.data['nombre']

        if Etiqueta.objects.filter(nombre = nombre).exists():
            return Response(status=status.HTTP_302_FOUND)
        else:
            etiqueta = Etiqueta.objects.create(nombre = nombre)
            etiqueta.save()
            
            return Response(status=status.HTTP_201_CREATED)

    def get(self, request, format=None):
        etiquetas = Etiqueta.objects.all()
        serializer = EtiquetaSerializer(etiquetas, many = True)
        
        return Response(serializer.data, status=status.Http_200_OK)
