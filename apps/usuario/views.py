from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.views import APIView
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
