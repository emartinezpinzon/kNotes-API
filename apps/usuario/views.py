from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
import json

from apps.usuario.models import Autor

class RegistroAutorList(APIView):
    def post(self, request, format = None):
        nombre = request.data['nombre']
        email = request.data['email']
        password = request.data['password']

        if User.objects.filter(username = email).exists():
            return Response(status = status.HTTP_302_FOUND)
        else:
            user = User.objects.create_user(email, email, password)
            user.save()

            autor = Autor(nombre = nombre, user = user)
            autor.save()

            return Response(status = status.HTTP_201_CREATED)

class LoginList(APIView):
    def post(self, request, format = None):
        email = request.data['email']
        password = request.data['password']

        user = authenticate(username = email, password = password)

        try:
            us = Autor.objects.get(user__username = email)

            if user is not None:
                try:
                    token=Token.objects.create(user = user)
                except:
                    token=Token.objects.get(user = user)

                objeto={'token':token.key,'iduser':us.pk}

                return HttpResponse(json.dumps(objeto),content_type="application/json")
            else:
                return Response(status = status.HTTP_403_FORBIDDEN)
        except Autor.DoesNotExist:
            mensaje = "Autor no existe"
            return Response(mensaje, status = status.HTTP_401_UNAUTHORIZED)
