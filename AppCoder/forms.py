from django import forms
from .models import *

class formularioAutos(forms.Form):
    id = models.AutoField(auto_created=True, primary_key=True)
    nombre = forms.CharField()
    anio = forms.IntegerField()
