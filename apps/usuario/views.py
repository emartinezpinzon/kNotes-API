from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
import json

#Registro de nuevos usuarios
class RegistroList(APIView):
    def post(self, request, format = None):
        nombre = request.data['nombre']
        apellido = request.data['apellido']
        email = request.data['email']
        password = request.data['password']

        if User.objects.filter(username=email).exists():
            return Response(status=status.HTTP_302_FOUND)
        else:
            user = User.objects.create_user(email, email, password, first_name=nombre, last_name=apellido)
            user.save()

            return Response(status=status.HTTP_201_CREATED)

#Inicio de sesión para usuarios registrados
class LoginList(APIView):
    def post(self, request, format=None):
        email = request.data['email']
        password = request.data['password']

        user = authenticate(username=email, password=password)

        try:
            us = User.objects.get(username=email)

            if user is not None:
                try:
                    token=Token.objects.create(user=user)
                except:
                    token=Token.objects.get(user=user)

                objeto={'token':token.key,'iduser':us.pk}

                return HttpResponse(json.dumps(objeto),content_type="application/json")
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except User.DoesNotExist:
            mensaje="Usuario no existe"
            return Response(mensaje, status = status.HTTP_401_UNAUTHORIZED)
