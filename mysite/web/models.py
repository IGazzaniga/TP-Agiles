import datetime
from django.db import models
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