from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Actividad(models.Model):
    nombre = models.CharField(max_length=32)
    horario = models.TimeField()

class Persona(models.Model):
    nombre = models.CharField(max_length=32)
    grado = models.CharField(max_length=32)
    esProfe = models.BooleanField(default=False)
    actividad = models.ForeignKey(Actividad)
