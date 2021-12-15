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

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")
    
def entregables(request):
    return render(request, "AppCoder/entregables.html")