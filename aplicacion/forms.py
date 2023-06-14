from .models import Usuario
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class frmUsuario(UserCreationForm):
    pass
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1",'password2']

class frmPerfil_ext(forms.ModelForm):

    class Meta:
        model=Usuario
        fields=["rut","direccion"]