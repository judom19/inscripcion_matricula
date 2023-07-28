from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import index_usuarios, Registro_usuario, EncargadoListView

app_name = 'app_usuarios'

urlpatterns = [
    path('index', login_required(index_usuarios), name='index_usuarios'),
    path('nuevo', login_required(Registro_usuario.as_view()), name='nuevo'),
    path('listado', login_required(EncargadoListView.as_view()), name='listado'),
]
