from django import forms
from .models import *

class formularioAutos(forms.Form):
    nombre = forms.CharField()
    anio = forms.IntegerField()
