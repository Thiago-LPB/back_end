from rest_framework import serializers
from .models import Financiador, AreaTecnologica, Colaborador, Projeto

class FinanciadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financiador
        fields = '__all__'


class AreaTecnologicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaTecnologica
        fields = '__all__'


class ColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        fields = '__all__'


class ProjetoSerializer(serializers.ModelSerializer):
    qtd_membros = serializers.IntegerField(read_only=True)

    class Meta:
        model = Projeto
        fields = '__all__'
