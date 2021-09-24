"""Hace el llamado a todo el código del sistema, todo se accesa por una URL"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluimos las urls de la app dependencia
    path('', include('applications.home.urls')),
    path('', include('applications.dependencia.urls')),
    path('', include('applications.empleado.urls'))
]
