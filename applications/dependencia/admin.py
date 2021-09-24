from django.contrib import admin
from .models import Dependencia, Sede
# Register your models here.

class DependenciaAdmin(admin.ModelAdmin):
    list_display=(
        'nombre',
        'sigla',
        'activa',
        'piso', 
        'lado',
        'oficina',
        'sede',)
    search_fields=(
        'nombre',
        'sigla',
    )
    list_filter=(
        'activa',
        'sede',
    )

admin.site.register(Dependencia, DependenciaAdmin)

class SedeAdmin (admin.ModelAdmin):
    list_display = (
        'nombre',
        'activa',
        'calle',
        'numero',
    )
admin.site.register(Sede,SedeAdmin)