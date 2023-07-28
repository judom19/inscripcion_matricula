from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import index_docentes, index_secciones, \
    DocenteCreateView, DocenteListView, DocenteUpdateView, DocenteDeleteView, \
    SeccionesCreateView, SeccionesListView

app_name = 'app_docentes'


urlpatterns = [
    path('index', login_required(index_docentes), name='index_docentes'),
    path('nuevo', login_required(DocenteCreateView.as_view()), name='nuevo'),
    path('listado', login_required(DocenteListView.as_view()), name='listado'),
    path('editar/<int:pk>/', login_required(DocenteUpdateView.as_view()), name='editar'),
    path('borrar/<int:pk>/', login_required(DocenteDeleteView.as_view()), name='borrar'),
    path('index_secciones', login_required(index_secciones), name='index_secciones'),
    path('nuevas_secciones', login_required(SeccionesCreateView.as_view()), name='nuevas_secciones'),
    path('listados_secciones', login_required(SeccionesListView.as_view()), name='listados_secciones'),
]
