from django.db import models
from django.contrib.auth.models import User

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    posicion = models.CharField(max_length=50)
    equipo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
