from django.db import models
from app_alumnos.models import Alumno
class Encargado(models.Model):
    # DATOS ENCARGADO
    dui = models.CharField(blank=True, max_length=100, help_text="Ingrese número de DUI sin guiones")
    alumno = models.OneToOneField('app_alumnos.Alumno', on_delete=models.SET_NULL, null=True, blank=True)
    nombre_encargado = models.CharField(null=True, blank=True, max_length=60, help_text="Ingrese un nombre válido")
    apellido_encargado = models.CharField(blank=False, max_length=60)
    fecha_nacimiento_encargado = models.DateField(blank=True, null=True)

    # Datos PADRES DEL Alumno
    nombre_madre = models.CharField(null=True, blank=True, max_length=60)
    dui_madre = models.CharField(null=True, blank=True, max_length=60)
    ocupacion_madre = models.CharField(null=True, blank=True, max_length=60)
    nombre_padre = models.CharField(null=True, blank=True, max_length=60)
    dui_padre = models.CharField(null=True, blank=True, max_length=60)
    ocupacion_padre = models.CharField(null=True, blank=True, max_length=60)

    def __str__(self):
        return self.nombre_encargado
