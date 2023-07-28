from django.db import models

class Secciones(models.Model):
    opciones_turnos = (
        ('MATUTINO', 'MATUTITO'),
        ('TARDE', 'TARDE'),
        ('FIN DE SEMANA', 'FIN DE SEMANA')
    )
    turno = models.CharField(max_length=40, choices=opciones_turnos, default='MATUTITO')
    nombre_seccion = models.CharField(blank=False, max_length=30)
    cupor_por_seccion = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre_seccion

class Docente(models.Model):
    dui_docente = models.CharField(blank=False, max_length=30, default='')
    nombre = models.CharField(blank=False, max_length=30)
    apellido = models.CharField(blank=False, max_length=30)
    nip_docente = models.CharField(blank=False, max_length=20, null=True)
    seccion_cargo = models.ForeignKey(Secciones, null=True, blank=True, on_delete=models.SET_NULL)
    alumnos_a_cargo = models.ForeignKey('app_alumnos.Alumno', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre
