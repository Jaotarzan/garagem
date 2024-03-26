from rest_framework.serializers import ModelSerializer

from Garagem.models import Acessório, Categoria, Cor, Marca, Veículo

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"

class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = Acessório
        fields = "__all__"

class CorSerializer(ModelSerializer):
    class Meta:
        model = Cor
        fields = "__all__"

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veículo
        fields = "__all__"

class VeiculoListSerializer(ModelSerializer):
    class Meta:
        model = Veículo
        fields = ["id", "modelo", "ano"]

class VeiculoDetailSerializer(ModelSerializer):
    class Meta:
        model = Veículo
        fields = "__all__"
        depth = 1