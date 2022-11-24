from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE


# Create your models here.
class Estudiante(models.Model):
    usuario = models.OneToOneField(User, null=True, on_delete=CASCADE)
    anno = models.PositiveIntegerField(verbose_name="Año", null=True)
    grupo = models.ForeignKey('Grupo', on_delete=CASCADE)

    def __str__(self):
        return self.usuario.first_name + " " + self.usuario.last_name

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'


class Profesor(models.Model):
    usuario = models.OneToOneField(User, null=True, on_delete=CASCADE)
    grupo = models.OneToOneField('Grupo',null=True, on_delete=CASCADE)
    departamento = models.TextField()
    solapin = models.TextField()

    def __str__(self):
        return self.usuario.first_name + " " + self.usuario.last_name

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'


class Caracterizacion(models.Model):
    anno = models.PositiveIntegerField(verbose_name='Año', null=True)
    investigacion = models.TextField(verbose_name='Investigacion')
    cultura = models.TextField(verbose_name='Cultura')
    docencia = models.TextField(verbose_name='Docencia')
    extension = models.TextField(verbose_name='Extension')
    estudiante = models.ForeignKey('Estudiante', on_delete=CASCADE)
    creado = models.DateTimeField(auto_now_add=True, null=True)
    modificado = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Caracterizacion'
        verbose_name_plural = 'Caracterizaciones'

    def __str__(self):
        return "Caracterizacion de " + str(self.anno) + " año de " + self.estudiante.usuario.first_name


class Evaluacion(models.Model):
    nota = models.IntegerField()
    caracterizacion = models.OneToOneField('Caracterizacion', null=True, on_delete=CASCADE)
    profesor = models.ForeignKey('Profesor', null=True, on_delete=CASCADE)

    def __str__(self):
        return "Evaluacion " + str(self.id)

    class Meta:
        verbose_name = 'Evaluacion'
        verbose_name_plural = 'Evaluaciones'

class Grupo(models.Model):
    numero = models.IntegerField()

    def __str__(self):
        return str(self.numero)
    