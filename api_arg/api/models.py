from django.db import models

# Create your models here. tablas de la bd


class Jugadores(models.Model):
    nombre = models.CharField(max_length=150)
    edad = models.IntegerField()
    imagen = models.URLField(help_text="Cargar solo la url")
    descripcion = models.TextField(help_text="Descripcion breve del jugador")

    class Meta:
        ordering = ["nombre"]
