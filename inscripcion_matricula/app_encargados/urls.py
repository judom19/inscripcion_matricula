from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import index_encargados, EncargadoListView, EncargadoCreateView

app_name = 'app_encargados'

urlpatterns = [
    path('index', login_required(index_encargados), name='index_encargados'),
    path('listado', login_required(EncargadoListView.as_view()), name='listado'),
    path('nuevo', login_required(EncargadoCreateView.as_view()), name='nuevo'),
]
