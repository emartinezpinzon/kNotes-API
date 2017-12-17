from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User

from apps.nota.models import *
from apps.nota.serializers import *

class EtiquetaList(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes=(IsAuthenticated, )

    #Registra una etiqueta
    def post(self, request, format=None):
        nombre = request.data['nombre']
        autor = User.objects.get(id=request.user.id)

        if Etiqueta.objects.filter(nombre=nombre).filter(autor_id=autor.id).exists():
            return Response(status=status.HTTP_302_FOUND)
        else:
            etiqueta = Etiqueta.objects.create(nombre=nombre, autor=autor)
            etiqueta.save()
            
            return Response(status=status.HTTP_201_CREATED)

    #Lista las etiquetas del autor
    def get(self, request, format=None):
        etiquetas = Etiqueta.objects.filter(autor_id=request.user.id)
        serializer = EtiquetaSerializer(etiquetas, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class EtiquetaDetail(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes=(IsAuthenticated, )

    #Obtiene una etiqueta por su ID
    def get_object(self, pk):
        try:
            return Etiqueta.objects.get(pk=pk)
        except Etiqueta.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    #Obtiene la información de una etiqueta
    def get(self, request, pk, format=None):
        etiqueta = self.get_object(pk)
        serializer = EtiquetaSerializer(etiqueta)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    #Actualiza la información de una etiqueta
    def put(self, request, pk, format=None):
        etiqueta = self.get_object(pk)
        serializer = EtiquetaSerializer(etiqueta, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Elimina una etiqueta
    def delete(self, request, pk, format=None):
        etiqueta = self.get_object(pk)
        etiqueta.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)

class NotaList(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes=(IsAuthenticated, )

    #Registra una nota
    def post(self, request, format=None):
        titulo = request.data['titulo']
        contenido = request.data['contenido']
        etiqueta = request.data['etiqueta']

        nota = Nota.objects.create(titulo=titulo, contenido=contenido, autor_id=request.user.id, etiqueta_id=etiqueta)
        nota.save()

        return Response(status=status.HTTP_201_CREATED)

    #Obtiene una lista de todas las notas del autor
    def get(self, request, format=None):
        notas = Nota.objects.filter(autor_id=request.user.id)
        serializer = NotaSerializer(notas, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class NotaDetail(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes=(IsAuthenticated, )

    #Obtiene una nota por su ID
    def get_object(self, pk):
        try:
            return Nota.objects.get(pk=pk)
        except Nota.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    #Obtiene la información de una nota
    def get(self, request, pk, format=None):
        nota = self.get_object(pk)
        serializer = NotaSerializer(nota)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    #Actualiza la información de una nota
    def put(self, request, pk, format=None):
        nota = self.get_object(pk)

        titulo = request.data['titulo']
        contenido = request.data['contenido']
        etiqueta_id = request.data['etiqueta_id']

        try:
            nota.titulo = titulo
            nota.contenido = contenido
            nota.etiqueta_id = etiqueta_id
            
            nota.save()
            
            return Response(status=status.HTTP_200_OK)
        except Etiqueta.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    #Elimina una nota
    def delete(self, request, pk, format=None):
        nota = self.get_object(pk)
        nota.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)

class NotasEtiquetaList(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes=(IsAuthenticated, )

    #Obtiene una lista de todas las notas por etiqueta
    def get(self, request, pk, format=None):
        notatag = Nota.objects.filter(etiqueta_id=pk)
        serializer = NotaSerializer(notatag, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
