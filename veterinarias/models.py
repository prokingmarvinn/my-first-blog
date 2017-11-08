from django.db import models
from django.contrib import admin

# Create your models here.
class Pasciente(models.Model):

    nombre  =   models.CharField(max_length=30)
    dueño  =   models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    def __str__(self):
        return self.nombre

class Veterinario(models.Model):

    nombre    = models.CharField(max_length=60)

    edad      = models.IntegerField()
    pascientes   = models.ManyToManyField(Pasciente, through='Consulta')
    def __str__(self):
        return self.nombre
class Consulta (models.Model):
    fecha_consulta = models.DateField()
    Pasciente = models.ForeignKey(Pasciente, on_delete=models.CASCADE)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
class ConsultaInLine(admin.TabularInline):

    model = Consulta
#muestra un campo extra al momento de insertar, como indicación que se pueden ingresar N actores.
    extra = 1
class PascienteAdmin(admin.ModelAdmin):
    inlines = (ConsultaInLine,)
class VeterinarioAdmin (admin.ModelAdmin):
    inlines = (ConsultaInLine,)
