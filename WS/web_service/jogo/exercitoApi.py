from rest_framework import serializers
from jogo.models import Exercito
from usuario.models import Usuario

class ExercitoApi(serializers.HyperlinkedModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    
    class Meta:
        model = Exercito
        fields = ('id','nome','slogan','cor','bandeira', 'usuario')