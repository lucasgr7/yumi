from django.db import models
import usuario

# Create your models here.
class Exercito(models.Model):
    nome = models.CharField(max_length=60)
    slogan = models.CharField(max_length=128)
    bandeira = models.CharField(max_length=300)
    cor = models.CharField(max_length=30)
    usuario = models.ForeignKey(usuario.models.Usuario)
    
