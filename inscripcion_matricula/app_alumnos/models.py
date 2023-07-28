from django.db import models
from datetime import datetime
from app_docentes.models import Docente

class Alumno(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    fecha_inscripcion = models.DateField(default=datetime.now)
    docente_encargado = models.ForeignKey('app_docentes.Docente', on_delete=models.SET_NULL, null=True, blank=True)
    direccion_actual = models.CharField(max_length=60, null=True, blank=True)
    telefono_actual_casa = models.CharField(max_length=60, null=True, blank=True)
    ultimo_centro_de_estudio = models.CharField(max_length=60, null=True, blank=True)
    comentarios = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombre

