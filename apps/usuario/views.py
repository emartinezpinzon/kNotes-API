from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
import json

from apps.usuario.models import Autor

class RegistroAutorList(APIView):
    def post(self,request,format=None):
        nombre = request.data['nombre']
        email = request.data['email']
        password = request.data['password']

        if User.objects.filter(username=email).exists():
            return HttpResponse("Existe")
        else:
            user = User.objects.create_user(email, email, password)
            user.save()

            autor=Autor(nombre=nombre, user=user)
            autor.save()

            return HttpResponse("Registrado")

class LoginList(APIView):
    def post(self, request, format=None):
        email = request.data['email']
        password = request.data['password']

        user = authenticate(username=email, password=password)

        try:
            us = Autor.objects.get(user__username=email)

            if user is not None:
                try:
                    token=Token.objects.create(user=user)
                except:
                    token=Token.objects.get(user=user)

                objeto={'token':token.key,'iduser':us.pk}

                return HttpResponse(json.dumps(objeto),content_type="application/json")
            else:
                objeto={'token':"Incorrecto"}
                
                return HttpResponse("Incorrecto")
        except Autor.DoesNotExist:
            objeto={'token':"No existe"}
            print(objeto)
            
            return HttpResponse("No existe")

    def get(self, request, format=None):
        return HttpResponseRedirect("/login/")
