from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Alumno
from .models import Encargado
from app_alumnos.forms import Alumno_Form
from .forms import Encargado_Form

def index_encargados(request):
    return render(request, 'index_principal_encargados.html')

class EncargadoListView(ListView):
    model = Encargado
    template_name = 'listado_encargados.html'

class EncargadoCreateView(CreateView):
    model = Encargado
    form_class = Encargado_Form
    second_form_class = Alumno_Form
    template_name = 'CRUD_encargados.html'
    success_url = reverse_lazy('app_encargados:listado')

    def get_context_data(self, **kwargs):
        context = super(EncargadoCreateView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            encargado = form.save(commit=False)
            encargado.alumno = form2.save()
            encargado.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))
