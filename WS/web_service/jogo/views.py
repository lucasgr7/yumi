from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from usuario.models import Usuario
from jogo.models import Exercito, Tatic, Soldado

from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
#import rest_framework_filters as filtro
from rest_framework.permissions import IsAdminUser
from django.shortcuts import HttpResponse
from django.core import serializers
from jogo.serializerApi import ExercitoApi, TaticApi, SoldadoApi
import json

# Create your views here.


def inserir_exercito(request):
    if request.method == 'POST':
        dados = json.loads(request.body)
        # print dados
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
    # print exercitoApi
    return Response(exercitoApi.data)


def delete_exercito(request, codigo):
    exercito = Exercito.objects.get(pk=codigo)
    exercito.delete()
    return HttpResponse('DELETE - OK')


def inserir_tatic(request):
    if request.method == 'POST':
        dados = json.loads(request.body)
        # print dados
        if 'id' not in dados:
            dados['id'] = None

        new_tatic = Tatic(
                        id=dados['id'],
                        nome=dados['nome'],
                        foto=dados['foto'],
                        required_ofensa=dados['required_ofensa'],
                        required_defesa=dados['required_defesa'],
                        required_estrategia=dados['required_estrategia']
                        )
    new_tatic.save()
    return HttpResponse('INSERT - OK')


@api_view(['GET'])
def list_tatic(request):
    tatics = Tatic.objects.all()
    taticApi = TaticApi(tatics, many=True)
    # print exercitoApi
    return Response(taticApi.data)


def inserir_soldado(request):
    if request.method == 'POST':
        dados = json.loads(request.body)
        # print dados
        if 'id' not in dados:
            dados['id'] = None

        soldado = Soldado(
                        id=dados['id'],
                        nome=dados['nome'],
                        foto=dados['foto'],
                        forca=dados['forca'],
                        escudo=dados['escudo'],
                        mira=dados['mira'],
                        max_hp=dados['max_hp'],
                        hp=dados['hp'],
                        tatics_ofensa=dados['tatics_ofensa'],
                        tatics_defesa=dados['tatics_defesa'],
                        tatics_estrategia=dados['tatics_estrategia']
                        )

    soldado.save(force_insert=False, force_update= False if dados['id'] == None else True)
    return HttpResponse('INSERT - OK')


@api_view(['GET'])
def list_soldado(request):
    soldados = Soldado.objects.all()
    soldadoApi = SoldadoApi(soldados, many=True)
    return Response(soldadoApi.data)


def delete_soldado(request, codigo):
    soldado = SoldadoApi.objects.get(pk=codigo)
    soldado.delete()
    return HttpResponse('DELETE - OK')