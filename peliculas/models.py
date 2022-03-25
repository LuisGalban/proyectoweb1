from django.db import models
from django.db.models.base import Model, ModelStateFieldsCacheDescriptor
from django.db.models.fields.related import create_many_to_many_intermediary_model

# Create your models here.

class genero(models.Model):

    nombre = models.CharField(max_length = 55)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:

        verbose_name = "genero"
        verbose_name_plural = "generos"
    
    def __str__(self):
        return self.nombre

class fecha(models.Model):

    año = models.CharField(max_length=55)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:

        verbose_name = "fecha"
        verbose_name_plural = "fechas"
    
    def __str__(self):
        return self.año


class pelicula(models.Model):
    titulo = models.CharField(max_length = 55)
    psinopsis = models.CharField(max_length = 1000)
    imagen = models.ImageField(upload_to = "peliculas")
    fecha = models.ManyToManyField(fecha)
    genero = models.ManyToManyField(genero)
    link = models.URLField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = "pelicula"
        verbose_name_plural = "peliculas"

    def __str__(self):
        return self.titulo


