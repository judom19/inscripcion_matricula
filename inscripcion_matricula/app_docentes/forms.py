from django import forms
from .models import Docente,Secciones# importando modelo alumno


class Docente_Form(forms.ModelForm):
    class Meta:
        model=Docente

        fields = [
            'nombre',
            'apellido',
            'seccion_cargo',
            'dui_docente',
            'nip_docente',

        ]
        seccion_cargo = forms.ModelChoiceField(
        queryset=Secciones.objects.all(),  # Aquí usamos el nombre correcto del modelo 'Secciones'
        label='Sección a cargo',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
        labels = {
            'nombre'  :'Nombre',
            'apellido' :'Apellido',
            'seccion_cargo' :'GRADO',
            'cedula':'Cedula',
            'doc_id':'Identificacón Educador',

        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'apellido':forms.TextInput(attrs={'class':'form-control'}),
            'seccion_cargo':forms.Select(attrs={'class':'form-control'}),
            'dui_docente':forms.TextInput(attrs={'class':'form-control'}),
            'nip_docente':forms.TextInput(attrs={'class':'form-control'}),

        }


class Secciones_Form(forms.ModelForm):
    class Meta:
        model=Secciones

        fields = [
            'turno',
            'nombre_seccion',
            'cupor_por_seccion',




        ]
        labels = {
            'turno'  :'Turno',
            'nombre_seccion' :'Nombre de la Seccion',
            'cupor_por_seccion' :'Cupo de esta seccion',


        }
        widgets = {
            'turno' : forms.Select(attrs={'class':'form-control'}),
            'nombre_seccion':forms.TextInput(attrs={'class':'form-control'}),
            'cupor_por_seccion':forms.TextInput(attrs={'class':'form-control'}),

        }
