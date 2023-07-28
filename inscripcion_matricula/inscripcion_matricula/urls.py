from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_alumnos.urls')),
    path('docentes/', include('app_docentes.urls')),
    path('encargados/', include('app_encargados.urls')),
    path('usuarios/', include('app_usuarios.urls')),
]

