from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from Garagem.models import Marca
from Garagem.serializers import MarcaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer        