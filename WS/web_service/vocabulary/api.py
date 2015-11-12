from rest_framework import serializers
from vocabulary.models import Personage

class PersonageApi(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Personage
        fields = ('id', 'name', 'sex', 'description')