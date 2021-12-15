from django.urls import path

from AppCoder import views

urlpatterns = [

    path("", views.inicio, name= "Inicio"),
    path('autos', views.autos, name="Autos"),
    path('marcas', views.marcas, name="Marcas"),
    path('estudiantes', views.modelos, name="Modelos"),
    path('clasificaciones', views.clasificaciones, name="Clasificaciones"),
    path('formularioAutos', views.formularioAutos, name="FormulariosAutos" ),

]
