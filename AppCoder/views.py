from django.http.response import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

# Create your views here.
def curso(self):
    curso = Curso(nombre="Desarrollo Web", camada="18998")
    curso.save()
    documentoDeTexto = f"----> Curso: {curso.nombre}   Camada: {curso.camada}"

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