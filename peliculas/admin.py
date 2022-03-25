from django.contrib import admin
from .models import pelicula, genero, fecha

# Register your models here.

class peliculaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class generoAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class fechaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(pelicula, peliculaAdmin)
admin.site.register(genero, generoAdmin)
admin.site.register(fecha, fechaAdmin)