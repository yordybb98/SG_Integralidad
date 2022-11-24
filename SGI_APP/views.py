from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from SGI_APP.models import Evaluacion, Caracterizacion, Estudiante, Profesor


# Create your views here.

@login_required
def home(request):
    try:
        if request.user.estudiante:
            nombre = "Evaluaciones"
            return render(request, 'home-est.html',{"nombre":nombre})
    except Estudiante.DoesNotExist :
        try:
            if request.user.profesor:
                nombre = "Caracterizaciones"
                return render(request,'home-prof.html',{"nombre":nombre})
        except Profesor.DoesNotExist:
            if request.user.is_staff:
                return redirect('/admin')
            


@login_required
def autoevaluaciones(request):
    try:    
        if request.user.estudiante:
            list_evaluaciones = Evaluacion.objects.filter(
                caracterizacion__estudiante__usuario__username=request.user.username).order_by('caracterizacion__anno')
            nombre = "Evaluaciones"
            return render(request, 'autoevaluaciones-est.html', {"list_e": list_evaluaciones, "nombre":nombre})
    except Estudiante.DoesNotExist:
        try:
            if request.user.profesor:
                try:
                    if request.method =='POST':
                        investigacion = request.POST['investigacion']
                        cultura = request.POST['cultura']
                        docencia = request.POST['docencia']
                        extension = request.POST['extension']
                        nota = request.POST['nota']
                        id_caracterizacion = request.GET['id_caract']
                        caract = Caracterizacion.objects.get(id = id_caracterizacion)

                        caract.cultura = cultura
                        caract.docencia = docencia
                        caract.extension = extension
                        caract.investigacion = investigacion
                        caract.save()

                        evaluacion = Evaluacion.objects.get(caracterizacion = caract)
                        evaluacion.nota = nota
                        evaluacion.profesor = request.user.profesor
                        evaluacion.save()
                        messages.add_message(request,messages.SUCCESS, 'Evaluacion Realizada')
                except ValueError:
                    messages.add_message(request,messages.INFO, 'No se realizo la Evaluacion')
                    
                list_evaluaciones = Evaluacion.objects.filter(
                    caracterizacion__estudiante__grupo__numero = request.user.profesor.grupo.numero).order_by('caracterizacion__anno')
                evaluacion_1=list_evaluaciones.filter(caracterizacion__anno=1)
                evaluacion_2=list_evaluaciones.filter(caracterizacion__anno=2)
                evaluacion_3=list_evaluaciones.filter(caracterizacion__anno=3)
                evaluacion_4=list_evaluaciones.filter(caracterizacion__anno=4)
                print (list_evaluaciones)
                nombre = "Caracterizaciones"
                return render(request,'autoevaluaciones-prof.html',{"list_eval":list_evaluaciones, "nombre":nombre,
                                                                    "evaluacion_1":evaluacion_1,"evaluacion_2":evaluacion_2,
                                       "evaluacion_3":evaluacion_3,"evaluacion_4":evaluacion_4})
        except Profesor.DoesNotExist:
            return HttpResponse('NO TIENE PERMISOS')


def Login(request):
    if request.method == 'POST':
        usuario: User = authenticate(username=request.POST['usuario'], password=request.POST['contrasena'])
        if usuario:
            login(request, usuario)
            return redirect('Home')
        messages.add_message(request, messages.ERROR, 'Usuario y/o Coontraseña incorrectos')
    return render(request, 'login.html')


@login_required
def caracterizacion(request):
    try:
        if(request.user.estudiante):
            haycaract = Caracterizacion.objects.filter(estudiante=request.user.estudiante, anno=request.GET['anno']).exists()
            if not haycaract:
                investigacion = request.POST['investigacion']
                cultura = request.POST['cultura']
                docencia = request.POST['docencia']
                extension = request.POST['extension']
                anno = request.GET['anno']
                estudiante = request.user.estudiante
                caracterizacion = Caracterizacion.objects.create(investigacion=investigacion, cultura=cultura,
                                                                docencia=docencia, extension=extension,
                                                                anno=anno, estudiante=estudiante)
                                                                
                evaluacion = Evaluacion.objects.create(nota = 0, caracterizacion=caracterizacion)
                messages.add_message(request, messages.SUCCESS, 'Caracterizacion Registrada')
                return redirect('Autoevaluaciones')
            messages.add_message(request, messages.ERROR, 'Ya Existe una Caracterizacion asignada a ese Año Academico')
            return redirect('Home')
    except Estudiante.DoesNotExist:
        return HttpResponse("SIN PERMISOS")

