from django.db import models
import usuario

# Create your models here.
class Exercito(models.Model):
    nome = models.CharField(max_length=60)
    slogan = models.CharField(max_length=128)
    bandeira = models.CharField(max_length=300)
    cor = models.CharField(max_length=30)
    usuario = models.ForeignKey(usuario.models.Usuario)
    
class Soldado(models.Model):
    nome = models.CharField(max_length=60)
    foto = models.CharField(max_length=300)
    level = models.CharField(max_length=1)
    forca = models.IntegerField(max_length=12)
    escudo = models.IntegerField(max_length=12)
    mira = models.IntegerField(max_length=12)
    max_hp = models.IntegerField(max_length=12)
    hp = models.IntegerField(max_length=12)
    tatics_ofensa = models.IntegerField(max_length=12)
    tatics_defesa = models.IntegerField(max_length=12)
    tatics_estrategia = models.IntegerField(max_length=12)
    
class Tatic(models.Model):
    nome = models.CharField(max_length=60)
    foto = models.CharField(max_length=300)
    required_ofensa = models.IntegerField(max_length=12)
    required_defesa = models.IntegerField(max_length=12)
    required_estrategia = models.IntegerField(max_length=12)
    
class Soldado_Tatic(models.Model):
    soldado = models.ForeignKey(Soldado)
    tatic = models.ForeignKey(Tatic)
    