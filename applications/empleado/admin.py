from django.contrib import admin
from .models import Empleado

class EmpleadoAdmin(admin.ModelAdmin):
    list_display=(
        'nombre',
        'apellido',
    )
    search_fields=(
            'nombre',
            'apellido',
            'dependencia',
        )
    filter_horizontal=(
            'dependencia',
        )

admin.site.register(Empleado,EmpleadoAdmin)
