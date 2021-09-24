from django.db import models

class Dependencia (models.Model):
    LADO_CHIOCES = (
        ('0', 'Frente'),
        ('1', 'Contrafrente'),
    )
    nombre = models.CharField('Nombre', max_length=70)
    sigla = models.CharField('Sigla', max_length=10, unique= True)
    activa = models.BooleanField('Activo')
    piso = models.IntegerField('Piso',null=True)
    lado = models.CharField('Lado', max_length=1, choices=LADO_CHIOCES,blank=True)
    oficina = models.CharField('Oficina', max_length=50, blank=True)
    sede  = models.ForeignKey('Sede', on_delete=models.CASCADE, verbose_name='Sede')    
    class Meta:
        verbose_name='Dependencia'
        verbose_name_plural = 'Dependencias'

    def __str__(self):
        return self.nombre + ' - ' + self.sigla

class Sede (models.Model):
    nombre = models.CharField('Nombre', max_length=70)
    activa = models.BooleanField('Activo')
    calle = models.CharField('Calle', max_length=70)
    numero = models.IntegerField ('Número',null=True)
 
    class Meta:
        verbose_name='Sede'
        verbose_name_plural = 'Sedes'

    def __str__(self):
        return self.nombre
