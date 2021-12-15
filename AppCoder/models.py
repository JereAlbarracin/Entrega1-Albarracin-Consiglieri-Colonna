from django.db import models

# Create your models here.
class Autos(models.Model):
    nombre = models.CharField(max_length=40)
    anio = models.IntegerField()

class Marcas(models.Model):
    nombre = models.CharField(max_length=30)
    estilo = models.CharField(max_length=30)
    

class ModeloCaracteristicas(models.Model):
    cantPersonas = models.IntegerField()
    caracteristica = models.CharField(max_length=30)
    ejes = models.IntegerField()

class Clasificaciones(models.Model):
    terreno = models.CharField(max_length=40)
    kilometros = models.IntegerField()
    duenios = models.IntegerField()
