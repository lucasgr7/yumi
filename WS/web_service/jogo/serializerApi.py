from rest_framework import serializers
from jogo.models import Exercito, Tatic, Soldado
from usuario.models import Usuario

# here will be create serialize-templates of jogos models

class ExercitoApi(serializers.HyperlinkedModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Exercito
        fields = ('id','nome','slogan','cor','bandeira', 'usuario')


class TaticApi(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tatic
        fields = ('id', 'nome', 'foto', 'required_ofensa', 'required_defesa', 'required_estrategia', 'chance', 'descricao')


class SoldadoApi(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Soldado
        fields = ('id', 'nome', 'foto', 'forca', 'escudo', 'mira', 'max_hp', 'hp', 'tatics_ofensa', 'tatics_defesa', 'tatics_estrategia')
