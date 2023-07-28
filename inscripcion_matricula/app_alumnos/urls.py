from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import index_alumnos, AlumnoListView, AlumnoCreateView, \
    AlumnoUpdateView, AlumnoDeleteView, AlumnoDetailView



app_name = 'app_alumnos'

# barra invertida para salto de línea
urlpatterns = [
    path('', login_required(index_alumnos), name='index_alumnos'),
    path('nuevo/', login_required(AlumnoCreateView.as_view()), name='nuevo'),
    path('listado/', login_required(AlumnoListView.as_view()), name='listado'),
    path('detalles/<int:pk>/', login_required(AlumnoDetailView.as_view()), name='detalles'),
    path('editar/<int:pk>/', login_required(AlumnoUpdateView.as_view()), name='editar'),
    path('borrar/<int:pk>/', login_required(AlumnoDeleteView.as_view()), name='borrar'),
]
