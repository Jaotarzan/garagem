from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from Garagem.models import Acessório, Categoria, Cor, Marca, Veículo
from Garagem.serializers import MarcaSerializer, AcessorioSerializer, CategoriaSerializer, CorSerializer, VeiculoSerializer, VeiculoListSerializer, VeiculoDetailSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class AcessorioViewSet(ModelViewSet):
    queryset = Acessório.objects.all()
    serializer_class = AcessorioSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veículo.objects.all()
    
    def get_serializer_class(self):
        if self.action == "list":
            return VeiculoListSerializer
        elif self.action == "retrieve":
            return VeiculoDetailSerializer
        return VeiculoSerializer