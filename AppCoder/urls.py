from django.urls import path

from AppCoder import views

urlpatterns = [

    path("", views.inicio, name= "Inicio"),
    path('autos', views.autos, name="Autos"),
    path('marcas', views.marcas, name="Marcas"),
    path('estudiantes', views.modelos, name="Modelos"),
    path('clasificaciones', views.clasificaciones, name="Clasificaciones"),
    path('busqueda', views.busqueda, name= "Busqueda"),
    path('formularioAutos', views.formularioAutos, name="FormulariosAutos" ),
    path('formularioMarcas', views.formularioMarcas, name="FormularioMarcas" ),
    path('formularioModelos', views.formularioModelos, name="FormularioModelos" ),
    path('formularioClasificaciones', views.formularioClasificaciones, name="FormularioClasificaciones" ),

]
