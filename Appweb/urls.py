from Appweb import views
from django.urls import path

urlpatterns = [
    path('', views.inicio, name= 'Inicio'),
    path('destino', views.Destinos, name= 'Destino'),
    path('pasajero', views.Pasajeros, name= 'Pasajero'),
    path('buscar', views.buscar, name= 'Buscar'),
    path('alojamiento', views.Alojamientos, name= 'Alojamiento'),
    path('leerPasajero', views.leerPasajeros, name= 'leerPasajero'),
    path('leerDestino', views.leerDestinos, name= 'leerDestino'),
    path('leerAlojamiento', views.leerAlojamientos, name= 'leerAlojamiento'),
]