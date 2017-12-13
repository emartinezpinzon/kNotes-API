from django.db import models
from django.contrib.auth.models import User

class Etiqueta(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Nota(models.Model):
    titulo=models.CharField(max_length=70)
    contenido=models.TextField(null=False)
    fecha=models.DateField(auto_now_add=True, null=False)
    autor=models.ForeignKey(User)
    disponible=models.BooleanField()

    def __str__(self):
        return self.titulo

class NotaEtiqueta(models.Model):
    etiqueta=models.ForeignKey(Etiqueta)
    nota=models.ForeignKey(Nota)

    def __str__(self):
        return str(self.etiqueta)+' - '+str(self.nota)
