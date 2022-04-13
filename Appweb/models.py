from django.db import models

class Destino(models.Model):
    lugar= models.CharField(max_length=30)
    fecha_desde= models.DateField()
    fecha_hasta= models.DateField()
    cantidad_de_personas= models.IntegerField()

    def __str__(self):
        return f"Destino: {self.lugar} - Fecha de viaje: {self.fecha_desde} al {self.fecha_hasta}. Viajan {self.cantidad_de_personas}"

class Pasajero(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    edad= models.IntegerField()

    def __str__(self):
        return f'Nombre: {self.nombre} {self.apellido}, edad {self.edad}. Contacto: {self.email}'

class Alojamiento(models.Model):
    nombre= models.CharField(max_length=30)
    direccion= models.CharField(max_length=50)

    def __str__(self):
        return f'Se aloja en {self.nombre}, direccion {self.direccion}'