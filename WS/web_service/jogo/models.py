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
    forca = models.IntegerField()
    escudo = models.IntegerField()
    mira = models.IntegerField()
    max_hp = models.IntegerField()
    hp = models.IntegerField()
    tatics_ofensa = models.IntegerField()
    tatics_defesa = models.IntegerField()
    tatics_estrategia = models.IntegerField()
    
class Tatic(models.Model):
    nome = models.CharField(max_length=60)
    foto = models.CharField(max_length=300)
    required_ofensa = models.IntegerField()
    required_defesa = models.IntegerField()
    required_estrategia = models.IntegerField()
    
class Soldado_Tatic(models.Model):
    soldado = models.ForeignKey(Soldado)
    tatic = models.ForeignKey(Tatic)
    