from django.db import models

# Create your models here.
class Usuario(models.Model):
    email = models.CharField(max_length=128)
    nome = models.CharField(max_length=128)
    senha = models.CharField(max_length=250)
    
