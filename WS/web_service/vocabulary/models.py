from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=20)
    localization = models.CharField(max_length=5)


class Personage(models.Model):
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=128)
    description = models.CharField(max_length=250)
    country = models.ForeignKey('Country')
    
