from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    cedula = models.CharField(max_length=150)
    telefono = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    estado = models.BooleanField(default=True)
    valor = models.IntegerField(default=0)
    
    

   
    