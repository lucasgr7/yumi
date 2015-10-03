from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from usuario.models import Usuario
from django.shortcuts import HttpResponse
import json

# Create your views here.
def inserir(request):
    if request.method == 'POST':
        dados = json.loads(request.body)
        
        usuario = Usuario(
                        email=dados['email'],
                        nome=dados['nome'],
                        senha=dados['senha']
                        )
    usuario.save()
    return HttpResponse('INSERT - OK')