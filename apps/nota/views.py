from django.shortcuts import render
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
    
    def post(self, request, format=None):
        nombre = request.data['nombre']
        autor = User.objects.get(id=request.user.id)

        if Etiqueta.objects.filter(nombre=nombre).filter(autor_id=autor.id).exists():
            return Response(status=status.HTTP_302_FOUND)
        else:
            etiqueta = Etiqueta.objects.create(nombre=nombre, autor=autor)
            etiqueta.save()
            
            return Response(status=status.HTTP_201_CREATED)

    def get(self, request, format=None):
        etiquetas = Etiqueta.objects.filter(autor_id=request.user.id)
        serializer = EtiquetaSerializer(etiquetas, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class EtiquetaDetail(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes=(IsAuthenticated, )
    
    def get_object(self, pk):
        try:
            return Etiqueta.objects.get(pk=pk)
        except Etiqueta.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        etiqueta = self.get_object(pk)
        serializer = EtiquetaSerializer(etiqueta)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        etiqueta = self.get_object(pk)
        serializer = EtiquetaSerializer(etiqueta, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        etiqueta = self.get_object(pk)
        etiqueta.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)

class NotaList(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes=(IsAuthenticated, )

    def post(self, request, format=None):
        
        print(request.data)
        
        titulo = request.data['titulo']
        contenido = request.data['contenido']
        etiquetas = request.data['etiquetas']

        nota = Nota.objects.create(titulo=titulo, contenido=contenido, autor_id=request.user.id)
        nota.save()


        print("--------------------------------     T     A     G     S     --------------------------------")
        print(etiquetas)

        for etiqueta in etiquetas:
            nota_etiqueta = NotaEtiqueta.objects.create(etiqueta_id=etiqueta, nota=nota)
            nota_etiqueta.save()

        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, format=None):
        notas = Nota.objects.filter(autor_id=request.user.id)
        serializer = NotaSerializer(notas, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class NotaDetail(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes=(IsAuthenticated, )

    def get_object(self, pk):
        try:
            return Nota.objects.get(pk=pk)
        except Nota.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        nota = self.get_object(pk)
        serializer = NotaSerializer(nota)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        nota = self.get_object(pk)
        serializer = NotaSerializer(nota, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        nota = self.get_object(pk)
        nota.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)

class EtiquetasNotaList(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes=(IsAuthenticated, )

    def post(self, request, pk, format=None):
        etiqueta_id = request.data['etiqueta_id']
        
        if NotaEtiqueta.objects.filter(etiqueta_id=etiqueta_id).filter(nota_id=pk).exists():
            return Response(status=status.HTTP_302_FOUND)
        else:
            etiqueta = Etiqueta.objects.get(id=etiqueta_id)
            nota = Nota.objects.get(id=pk)
            nota_etiqueta = NotaEtiqueta.objects.create(etiqueta=etiqueta, nota=nota)
            nota_etiqueta.save()

            return Response(status=status.HTTP_201_CREATED)

    def get(self, request, pk, format=None):
        notatag = NotaEtiqueta.objects.filter(nota_id=pk)
        serializer = NotaEtiquetaSerializer(notatag, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class NotasEtiquetaList(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes=(IsAuthenticated, )

    def get(self, request, pk, format=None):
        notatag = NotaEtiqueta.objects.filter(etiqueta_id=pk)
        serializer = NotaEtiquetaSerializer(notatag, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class NotaEtiquetaDetail(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes=(IsAuthenticated, )

    def get_object(self, pk):
        try:
            return NotaEtiqueta.objects.get(pk=pk)
        except NotaEtiqueta.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        notatag = self.get_object(pk)
        notatag.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
