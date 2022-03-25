from django.shortcuts import render
from .models import pelicula, genero, fecha

# Create your views here.

def home(request):
    return render(request, "peliculas/home.html")


def peliculas(request):
    peliculas = pelicula.objects.all()
    generos = genero.objects.all()
    fechas = fecha.objects.all()
    return render(request, "peliculas/peliculas.html",{"peliculas":peliculas, "generos":generos,'fechas':fechas})

def generos(request, genero_id):
    
    generos = genero.objects.get(id=genero_id)
    nombre_genero = genero.objects.all
    peliculas = pelicula.objects.filter(genero=generos)
    nombre_fecha = fecha.objects.all
    return render(request, "peliculas/generos.html", {'generos':generos,"peliculas":peliculas,'nombre_genero':nombre_genero,'nombre_fecha':nombre_fecha})

def movie(request, pelicula_id):
    
    movie = pelicula.objects.get(id=pelicula_id)
    nombre_genero = genero.objects.all
    peliculas = pelicula.objects.filter(titulo=movie)
    link = pelicula.objects.all()
    return render(request, "peliculas/movie.html", {'movie':movie,'nombre_genero':nombre_genero,'peliculas':peliculas, 'link':link})

def fechas(request, fecha_id):
    
    fechas = fecha.objects.get(id=fecha_id)
    nombre_genero = genero.objects.all
    nombre_fecha = fecha.objects.all
    peliculas = pelicula.objects.filter(fecha=fechas)
    return render(request, "peliculas/fechas.html", {'nombre_genero':nombre_genero,'nombre_fecha':nombre_fecha,'peliculas':peliculas})