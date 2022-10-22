from django.http import HttpResponse
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.template import Context, Template, loader
from django.shortcuts import render
import random

from home.models import Persona

def hola(request):
    return HttpResponse("home/<h1>Buenas clase</h1>")

def fecha(request):
    fecha_y_hora = datetime.now()
    return HttpResponse(f'home/La fecha y hora actual es {fecha_y_hora}')

def calcular_fecha_nacimiento(request, edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f'home/Tu fecha de nacimiento es: {fecha}')

def mi_template(request):
    cargar_archivo = open(r'C:\Users\Usuario\OneDrive\Escritorio\Coder_VSC\Practicas\django_Villanustre\templates\mi_template.html','r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)

def tu_template(request, nombre):
    #cargar_archivo = open(r'C:\Users\Usuario\OneDrive\Escritorio\Coder_VSC\Practicas\django_Villanustre\templates\tu_template.html','r')
    #template = Template(cargar_archivo.read())
    #cargar_archivo.close()
    #contexto = Context({'persona': nombre})
    #template_renderizado = template.render(contexto)

    template = loader.get_template('tu_template.html')
    template_renderizado = template.render({'persona': nombre})

    return HttpResponse(template_renderizado)

def prueba_template(request):
    
    mi_contexto = {
        'rango' : list(range(1,11)),
        'valor_aleatorio': random.randrange(1,11)
        }
    
    template = loader.get_template('prueba_template.html')
    template_renderizado = template.render(mi_contexto)

    return HttpResponse(template_renderizado)

def crear_persona(request):

    #nombre = request.POST
    #apellido = request.POST
    
    if request.method == 'POST':
        nombre= request.POST.get('nombre')
        apellido= request.POST.get('apellido')
    
        persona = Persona(nombre = nombre , apellido = apellido , edad= random.randrange(1,99), fecha_nacimiento=datetime.now())
        persona.save()
    #return render(request, 'home/crear_persona.html', {'persona': persona})

    template = loader.get_template('crear_persona.html')
    template_renderizado = template.render({})
    return HttpResponse(template_renderizado)

def ver_persona(request):

    personas = Persona.objects.all()
    
    #return render(request, 'ver_persona.html', {'personas': personas})

    template = loader.get_template('ver_persona.html')
    template_renderizado = template.render({'personas': personas})

    return HttpResponse(template_renderizado)

def index(request) :
        return render(request, 'index.html')