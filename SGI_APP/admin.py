from django.contrib import admin
from .models import Caracterizacion,Estudiante,Profesor,Evaluacion,Grupo

# Register your models here.


class CaracterizacionAdmin(admin.ModelAdmin):
    readonly_fields=('creado','modificado')


admin.site.register(Estudiante)
admin.site.register(Caracterizacion,CaracterizacionAdmin)
admin.site.register(Profesor)
admin.site.register(Evaluacion)
admin.site.register(Grupo)