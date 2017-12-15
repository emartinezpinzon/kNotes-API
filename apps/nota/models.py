from django.db import models
from django.contrib.auth.models import User

class Etiqueta(models.Model):
    nombre=models.CharField(max_length=50)
    autor=models.ForeignKey(User)

    def __str__(self):
        return self.nombre

class Nota(models.Model):
    titulo=models.CharField(max_length=70)
    contenido=models.TextField(null=False)
    fecha=models.DateField(auto_now_add=True, null=False)
    autor=models.ForeignKey(User)
    etiqueta=models.ForeignKey(Etiqueta)

    def __str__(self):
        return self.titulo
