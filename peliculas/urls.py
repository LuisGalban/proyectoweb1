from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name = 'home'),
    path('peliculas/',views.peliculas,name = 'peliculas'),
    path('generos/<int:genero_id>/',views.generos, name = "generos"),
    path('movie/<int:pelicula_id>/',views.movie,name = 'movie'),
    path('fechas/<int:fecha_id>/',views.fechas,name = 'fechas'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)