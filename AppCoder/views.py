from django.http.response import HttpResponse
from django.shortcuts import render
from AppCoder.models import *
from AppCoder.forms import formularioAutos

# Create your views here.
def auto(self):
    auto = Autos(nombre="Palio", anio="1998")
    auto.save()
    documentoDeTexto = f"----> Nombre: {auto.nombre}   Anio: {auto.anio}"

    return HttpResponse(documentoDeTexto)

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def autos(request):
    return render(request, "AppCoder/autos.html")

def marcas(request):
    return render(request, "AppCoder/marcas.html")

def modelos(request):
    return render(request, "AppCoder/modelos.html")
    
def clasificaciones(request):
    return render(request, "AppCoder/clasificaciones.html")

def busqueda(request):
    return render(request, "AppCoder/busqueda.html")

def formularioAutos(request):
    
    if request.method == "POST":

        #miFormulario = formularioAutos(request.POST)

        #print(miFormulario)
        
        #if miFormulario.is_valid:

            #informacion = miFormulario.formularioAutos(request.user)

            auto = Autos(nombre=request.POST['nombre'], anio=request.POST['anio'])
        
            auto.save()
        
            return render(request, "AppCoder/inicio.html")
    
    #else:
    #    miFormulario = formularioAutos()

    return render(request, "AppCoder/formularioAutos.html") #{"miFormulario":miFormulario})


def formularioMarcas(request):
    
    if request.method == "POST":


            marca = Marcas(nombre=request.POST['nombre'], estilo=request.POST['estilo'])
        
            marca.save()
        
            return render(request, "AppCoder/inicio.html")

    return render(request, "AppCoder/formularioMarcas.html")

def formularioModelos(request):
    
    if request.method == "POST":


            modelo = ModeloCaracteristicas(cantPersonas=request.POST['cantPersonas'], caracteristica=request.POST['caracteristica'], numeroDeEjes=request.POST['numeroDeEjes'])
        
            modelo.save()
        
            return render(request, "AppCoder/inicio.html")

    return render(request, "AppCoder/formularioModelos.html")

def formularioClasificaciones(request):
    
    if request.method == "POST":


            clasifica = Clasificaciones(terreno=request.POST['terreno'], kilometros=request.POST['kilometros'], duenios=request.POST['duenios'])
        
            clasifica.save()
        
            return render(request, "AppCoder/inicio.html")

    return render(request, "AppCoder/formularioClasificaciones.html")