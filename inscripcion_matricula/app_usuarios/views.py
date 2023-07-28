from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .form import Registro_form

# Create your views here.
def index_usuarios(request):
    return render(request, 'index_principal_usuarios.html')

class Registro_usuario(CreateView):
    model = User
    template_name = 'CRUD_usuarios.html'
    form_class = Registro_form
    success_url = reverse_lazy('app_usuarios:index_usuarios')

class EncargadoListView(ListView):
    model = User
    template_name = 'listado_usuarios.html'
