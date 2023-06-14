from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    rut=models.CharField(primary_key=True, max_length=10)
    usuario=models.OneToOneField(User,unique=True, related_name='perfil',on_delete=models.CASCADE)
    direccion=models.CharField(max_length=150)

class RegisterUserModel(models.Model):
    rut=models.CharField(max_length=10, unique=True)
    
