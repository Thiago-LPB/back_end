from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Financiador, AreaTecnologica, Colaborador, Projeto
from .serializers import FinanciadorSerializer, AreaTecnologicaSerializer, ColaboradorSerializer, ProjetoSerializer

class FinanciadorViewSet(viewsets.ModelViewSet):
    queryset = Financiador.objects.all()
    serializer_class = FinanciadorSerializer


class AreaTecnologicaViewSet(viewsets.ModelViewSet):
    queryset = AreaTecnologica.objects.all()
    serializer_class = AreaTecnologicaSerializer

class ColaboradorViewSet(viewsets.ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer


class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer

    @action(detail=True, methods=['post'])
    def inativar(self, request, pk=None):
        projeto = get_object_or_404(Projeto, pk=pk)
        projeto.inativar()
        return Response({'status': 'Projeto inativado'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def equipe(self, request, pk=None):
        projeto = get_object_or_404(Projeto, pk=pk)
        equipe = projeto.equipe.all()
        serializer = ColaboradorSerializer(equipe, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'])
    def equipe_atualizar(self, request, pk=None):
        projeto = get_object_or_404(Projeto, pk=pk)
        colaboradores_ids = request.data.get('equipe', [])
        colaboradores = Colaborador.objects.filter(id__in=colaboradores_ids)
        projeto.equipe.set(colaboradores)
        projeto.atualizar_qtd_membros()
        return Response({'status': 'Equipe atualizada'}, status=status.HTTP_200_OK)

