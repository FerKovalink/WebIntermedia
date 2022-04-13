from django.shortcuts import render
from django.http import HttpResponse
from Appweb.models import *
from Appweb.forms import *

def inicio(request):
    return render(request, 'Appweb/inicio.html')

def buscar(request):

      if request.GET['nombre']:
            nombre = request.GET['nombre']
            pasajero = Pasajero.objects.filter(nombre__icontains=nombre)

            return render(request, "Appweb/inicio.html", {"pasajero":pasajero, "nombre": nombre})

      else: 

	      respuesta = "No enviaste datos" 
      return HttpResponse(respuesta)


def Destinos(request):

      if request.method == 'POST':

            miFormulario = destinoFormulario(request.POST)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  destino = Destino (lugar=informacion['lugar'], fecha_desde=informacion['fecha_desde'], fecha_hasta=informacion['fecha_hasta'], cantidad_de_personas=informacion['cantidad_de_personas']) 

                  destino.save()

                  return render(request, "Appweb/inicio.html")

      else: 

            miFormulario= destinoFormulario()

      return render(request, "Appweb/destino.html", {"miFormulario":miFormulario})

def leerDestinos(request):

      destinos = Destino.objects.all()

      contexto= {"destinos":destinos} 

      return render(request, "Appweb/leerDestinos.html",contexto)



def Alojamientos(request):

      if request.method == 'POST':

            miFormulario = alojamientoFormulario(request.POST)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  alojamiento = Alojamiento (nombre=informacion['nombre'], direccion=informacion['direccion']) 

                  alojamiento.save()

                  return render(request, "Appweb/inicio.html")

      else: 

            miFormulario= pasajeroFormulario()

      return render(request, "Appweb/alojamiento.html", {"miFormulario":miFormulario})

def leerAlojamientos(request):

      alojamientos = Alojamiento.objects.all()

      contexto= {"alojamientos":alojamientos} 

      return render(request, "Appweb/leerAlojamientos.html",contexto)


def Pasajeros(request):

      if request.method == 'POST':

            miFormulario = pasajeroFormulario(request.POST)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  pasajero = Pasajero (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], edad=informacion['edad']) 

                  pasajero.save()

                  return render(request, "Appweb/inicio.html")

      else: 

            miFormulario= pasajeroFormulario()

      return render(request, "Appweb/pasajero.html", {"miFormulario":miFormulario})


def leerPasajeros(request):

      pasajeros = Pasajero.objects.all()

      contexto= {"pasajeros":pasajeros} 

      return render(request, "Appweb/leerPasajeros.html",contexto)
