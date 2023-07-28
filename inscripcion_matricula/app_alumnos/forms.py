from django import forms
from .models import Alumno

class Alumno_Form(forms.ModelForm):
    class Meta:
        model = Alumno

        fields = [
            'nombre',
            'apellido',
            'fecha_nacimiento',
            'docente_encargado',
            'direccion_actual',
            'telefono_actual_casa',
            'ultimo_centro_de_estudio',
            'comentarios',
        ]
        
        labels = {
            'nombre': 'Nombres del niño/a:',
            'apellido': 'Apellidos del niño/a:',
            'fecha_nacimiento': 'Fecha de Nacimiento:',
            'docente_encargado': 'Maestro encargado:',
            'comentarios': 'Comentarios:',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control'}),
            'docente_encargado': forms.Select(attrs={'class': 'form-control'}),
            'telefono_actual_casa': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_actual': forms.TextInput(attrs={'class': 'form-control'}),
            'ultimo_centro_de_estudio': forms.TextInput(attrs={'class': 'form-control'}),
            'comentarios': forms.Textarea(attrs={'class': 'form-control', 'cols': 3, 'rows': 3}),
        }
