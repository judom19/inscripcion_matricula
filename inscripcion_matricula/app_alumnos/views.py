from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import Alumno_Form
from .models import Alumno

def index_alumnos(request):
    return render(request,'index_principal.html')

class AlumnoListView(ListView):
    model = Alumno
    queryset = Alumno.objects.all()
    template_name = 'listado_alumnos.html'

class AlumnoDetailView(DetailView):
    model = Alumno
    queryset = Alumno.objects.all()
    template_name = 'detalles_alumnos.html'

class AlumnoCreateView(CreateView):
    model = Alumno
    form_class = Alumno_Form
    template_name = 'CRUD_alumnos.html'
    success_url = reverse_lazy('app_alumnos:index_alumnos')

class AlumnoUpdateView(UpdateView):
    model = Alumno
    form_class = Alumno_Form
    template_name = 'CRUD_alumnos.html'
    success_url = reverse_lazy('app_alumnos:index_alumnos')

    @method_decorator(permission_required('alumnos.change_alumno', reverse_lazy('app_alumnos:listado')))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class AlumnoDeleteView(DeleteView):
    model = Alumno
    template_name = 'eliminar_alumnos.html'
    success_url = reverse_lazy('app_alumnos:listado')


class AlumnoCreateView(CreateView):#vista basada en clases
    model = Alumno#indicando el nombre del modelo a usar
    form_class = Alumno_Form#atributo form class se usa
    # para guardar el formulario que hemos creado
    template_name = 'CRUD_alumnos.html'#se coloca el templateview
    #que se va a utilizar
    success_url = reverse_lazy('app_alumnos:index_alumnos')#indicando la url
    #a la que volvera luego de guardado el objeto
    #
    #
    #VISTA PARA EDITAR LOS OBJETOS ALUMNOS
class AlumnoUpdateView(UpdateView):
    model = Alumno#indicando el nombre del modelo a usar
    form_class = Alumno_Form#atributo form class se usa
    # para guardar el formulario que hemos creado
    template_name = 'CRUD_alumnos.html'#se coloca el templateview
    #que se va a utilizar
    success_url = reverse_lazy('alumnos:index_alumnos')#indicando la url
    #a la que volvera luego de guardado el objeto
    @method_decorator(permission_required('alumnos.changue_alumno',reverse_lazy('app_alumnos:listado')))
    def dispatch(self, *args, **kwargs):
            return super(AlumnoUpdateView, self).dispatch(*args, **kwargs)
class AlumnoDeleteView(DeleteView):
    model = Alumno
    template_name = 'eliminar_alumnos.html'
    success_url =reverse_lazy('app_alumnos:listado')
