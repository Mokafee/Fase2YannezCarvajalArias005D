from django.db import models
from django.urls import reverse  		#redirecciona una url de un libro al browser 
import uuid  							#se utiliza para definir atributos clave (pk)
# Create your models here.

class Genre(models.Model):
    #Model representing a book genre."""
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class formulario(models.Model):
    Nombre = models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    Telefono = models.IntegerField()
    Mensaje = models.CharField(max_length=5000)

    def __str__(self):
        return self.Nombre