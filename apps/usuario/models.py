from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    nombre=models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.nombre
