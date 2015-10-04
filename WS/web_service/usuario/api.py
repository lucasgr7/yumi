from rest_framework import serializers
from usuario.models import Usuario

class UsuarioApi(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id','nome','email')