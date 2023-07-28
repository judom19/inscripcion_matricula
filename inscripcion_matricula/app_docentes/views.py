from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import Docente_Form, Secciones_Form
from .models import Docente, Secciones

def index_docentes(request):
    return render(request, 'index_principal_docentes.html')

class DocenteListView(ListView):
    model = Docente
    context_object_name = 'docentes'
    template_name = 'listado_docentes.html'

class DocenteCreateView(CreateView):
    model = Docente
    form_class = Docente_Form
    template_name = 'CRUD_docentes.html'
    success_url = reverse_lazy('app_docentes:index_docentes')

class DocenteUpdateView(UpdateView):
    model = Docente
    form_class = Docente_Form
    template_name = 'CRUD_docentes.html'
    success_url = reverse_lazy('app_docentes:index_docentes')

class DocenteDeleteView(DeleteView):
    model = Docente
    template_name = 'eliminar_docentes.html'
    success_url = reverse_lazy('app_docentes:listado')

def index_secciones(request):
    return render(request, 'index_principal_secciones.html')

class SeccionesListView(ListView):
    model = Secciones
    template_name = 'listado_secciones.html'

class SeccionesCreateView(CreateView):
    model = Secciones
    form_class = Secciones_Form
    template_name = 'CRUD_secciones.html'
    success_url = reverse_lazy('app_docentes:listados_secciones')
