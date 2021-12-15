from django.http.response import HttpResponse
from django.shortcuts import render
from AppCoder.models import *

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

def formularioAutos(request):
    
    if request.method == "POST":
        
        auto = Autos (request.POST['nombre'], request.POST['anio'])
        
        auto.save()
        
        return render(request, "AppCoder/inicio.html")

    return render(request, "AppCoder/formularioAutos.html")