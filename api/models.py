from django.db import models

# Create your models here.

class User(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()
    email = models.CharField(max_length=50)
    
