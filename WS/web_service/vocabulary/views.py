from rest_framework.response import Response
from rest_framework.decorators import api_view
from vocabulary.api import PersonageApi
from vocabulary.models import Personage
import random

# Create your views here.

@api_view(['GET',])
def new_personage_name(request):
    # in current moment i don't use a filter - just random of all list
    # and don't take in account a gender
    max_random_value = Personage.objects.all().count();
    personage = Personage.objects.get(random.randint(1, max_random_value))
    personageApi = PersonageApi(personage, many=False)
    return Response(personageApi.data)
