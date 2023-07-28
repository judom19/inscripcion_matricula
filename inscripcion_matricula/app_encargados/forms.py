from django import forms
from .models import Encargado

class Encargado_Form(forms.ModelForm):
    class Meta:
        model = Encargado
        fields = [
            'nombre_encargado',
            'apellido_encargado',
            'dui',
            'fecha_nacimiento_encargado',
            'nombre_madre',
            'dui_madre',
            'ocupacion_madre',
            'nombre_padre',
            'dui_padre',
            'ocupacion_padre',
        ]
        labels = {
            'nombre_encargado': 'Nombre Encargado',
            'apellido_encargado': 'Apellido',
            'dui': 'DUI',
            'fecha_nacimiento_encargado': 'Fecha de Nacimiento de Encargado',
        }
        widgets = {
            'nombre_encargado': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_encargado': forms.TextInput(attrs={'class': 'form-control'}),
            'dui': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento_encargado': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_madre': forms.TextInput(attrs={'class': 'form-control'}),
            'dui_madre': forms.TextInput(attrs={'class': 'form-control'}),
            'ocupacion_madre': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_padre': forms.TextInput(attrs={'class': 'form-control'}),
            'dui_padre': forms.TextInput(attrs={'class': 'form-control'}),
            'ocupacion_padre': forms.TextInput(attrs={'class': 'form-control'}),
        }
