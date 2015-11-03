from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from usuario.models import Usuario
from jogo.models import Exercito

from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
#import rest_framework_filters as filtro
from rest_framework.permissions import IsAdminUser
from django.shortcuts import HttpResponse
from django.core import serializers
from jogo.exercitoApi import ExercitoApi
import json

# Create your views here.
def inserir_exercito(request):
    if request.method == 'POST':
        dados = json.loads(request.body)
        print dados
        if 'id' not in dados:
            dados['id'] = None
            
        usuario = Usuario.objects.get(pk=dados['usuario']['id'])
        exercito = Exercito(
                        id=dados['id'],
                        nome=dados['nome'],
                        slogan=dados['slogan'],
                        bandeira=dados['bandeira'],
                        cor=dados['cor'],
                        usuario=usuario
                        )
    exercito.save()
    return HttpResponse('INSERT - OK')

@api_view(['GET',])
def list_exercito(request):
    exercitos = Exercito.objects.all()
    exercitoApi = ExercitoApi(exercitos, many=True)
    print exercitoApi
    return Response(exercitoApi.data)

def delete(request, codigo):
    exercito = Exercito.objects.get(pk=codigo)
    exercito.delete()
    return HttpResponse('DELETE - OK')