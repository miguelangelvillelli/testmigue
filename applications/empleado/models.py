from django.db import models
from applications.dependencia.models import Dependencia
from ckeditor.fields import RichTextField

class Empleado(models.Model):
    nombre = models.CharField('Nombres', max_length=60)
    apellido = models.CharField('Apellidos', max_length=50)
#    dependencia = models.ForeignKey(Dependencia, on_delete=models.CASCADE, verbose_name='Dependencia')    
    dependencia = models.ManyToManyField(Dependencia)
    observaciones= RichTextField()
    

    def __str__(self):
        return self.nombre + ', ' + self.apellido.upper()
