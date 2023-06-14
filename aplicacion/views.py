from django.shortcuts import render
from .forms import frmPerfil_ext,frmUsuario
from django.contrib.auth.models import User
from .models import Usuario

# Create your views here.
def home(request):
    formext=frmPerfil_ext(request.POST or None)
    formnormal=frmUsuario(request.POST or None)
   
    contexto={
        "form":formext,
        "fuser":formnormal
        
    }

    if request.method=="POST":
        if formnormal.is_valid() and formext.is_valid():
            formnormal.save()
            datonormal=formnormal.cleaned_data
            usr=User.objects.get(username=datonormal.get("username"))
            u=Usuario()
            datos=formext.cleaned_data
            u.direccion=datos.get("direccion")
            u.rut=datos.get("rut")
            u.usuario=usr
            u.save()

    return render(request,"aplicacion/index.html",contexto)