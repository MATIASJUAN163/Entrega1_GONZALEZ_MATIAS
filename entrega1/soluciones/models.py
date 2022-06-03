from django.db import models

# Create your models here.

class Modem(models.Model): 

    marca = models.CharField( max_length=40 )
    modelo = models.CharField( max_length=40 )
    comunicacion = models.CharField( max_length=40 )
    precio = models.FloatField()

class Smartmeter(models.Model):

    marca = models.CharField( max_length=40 )
    modelo = models.CharField( max_length=40 )
    tipo = models.CharField(max_length=40 )
    precio = models.FloatField()

class Webclient(models.Model):

    marca = models.CharField( max_length=40 )
    modelo = models.CharField( max_length=40 )
    precio = models.FloatField()

