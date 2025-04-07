from django.db import models

# Create your models here.
# models.py
from django.contrib.auth.models import User

class Servicio(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class SolicitudServicio(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el cliente (usuario)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)  # Relación con el servicio
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    mensaje = models.TextField()
    estado = models.CharField(max_length=50, default='Pendiente')  # Ejemplo: 'Pendiente', 'En proceso', 'Completada'
    
    # Nuevos campos
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.cliente.username} - {self.servicio.nombre}"
