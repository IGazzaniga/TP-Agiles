import datetime
from django.db import models
from django.contrib import admin
from django.utils import timezone
# Create your models here.
class Novedad(models.Model):
    """Una novedad"""
    titulo = models.CharField(max_length=30) #Titulo de la novedad
    contenido = models.TextField() #Contenido de la novedad
    fechaP = models.DateTimeField('fecha de publicacion')
    tags = models.CharField(max_length=30)
    
    def was_published_recently(self):
        return self.fechaP >= timezone.now() - datetime.timedelta(days=1)

class Trabajo(models.Model):
    """Una oferta de trabajo"""
    titulo = models.CharField(max_length=30) #Titulo de la oferta
    descripcion = models.TextField() #Descripcion de la oferta
    fechaP = models.DateTimeField('fecha de publicacion')
    disponible = models.BooleanField(default=True) #True si la oferta sigue disponible, False en caso contrario

class Investigacion(models.Model):
    """Un tema de I+D"""
    titulo = models.CharField(max_length=30) #Titulo de la novedad
    autor = models.CharField(blank=True, max_length=200) #Quien investigo el tema
    archivo = models.FileField(blank=True, upload_to='web/uploads/%Y/%m/%d/')
    
    