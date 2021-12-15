from django.urls import path

from AppCoder import views

urlpatterns = [

    path("", views.inicio, name= "Inicio"),
    path('cursos', views.autos, name="Autos"),
    path('profesores', views.marcas, name="Marcas"),
    path('estudiantes', views.modelos, name="Modelos"),
    path('entregables', views.clasificaciones, name="Clasificaciones"),

]
