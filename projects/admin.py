from django.contrib import admin
from .models import Financiador, AreaTecnologica, Colaborador, Projeto

@admin.register(Financiador)
class FinanciadorAdmin(admin.ModelAdmin):
    list_display = ('id', 'financiador')

@admin.register(AreaTecnologica)
class AreaTecnologicaAdmin(admin.ModelAdmin):
    list_display = ('id', 'area_tecnologica')

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'dt_nascimento')

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('id', 'projeto', 'financiador', 'area_tecnologica', 'coordenador', 'ativo', 'qtd_membros')
    filter_horizontal = ('equipe',)
