from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from usuario.models import Usuario

from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
#import rest_framework_filters as filtro
from rest_framework.permissions import IsAdminUser
from django.shortcuts import HttpResponse
from django.core import serializers
from usuario.api import UsuarioApi
import json

# Create your views here.
def inserir(request):
    if request.method == 'POST':
        dados = json.loads(request.body)
        
        if 'id' not in dados:
            dados['id'] = None
            
        
        usuario = Usuario(
                        id=dados['id'],
                        email=dados['email'],
                        nome=dados['nome'],
                        senha=dados['senha']
                        )
    usuario.save()
    return HttpResponse('INSERT - OK')

@api_view(['GET',])
def list(request):
    usuarios = Usuario.objects.all()
    usuarioApi = UsuarioApi(usuarios, many=True)
    # print usuarioApi
    return Response(usuarioApi.data)

def delete(request, codigo):
    usuario = Usuario.objects.get(pk=codigo)
    usuario.delete()
    return HttpResponse('DELETE - OK')