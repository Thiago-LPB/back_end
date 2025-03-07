from django.db import models


class Financiador(models.Model):
    id = models.AutoField(primary_key=True)
    financiador = models.CharField(max_length=100)

class Colaborador(models.Model):
    id = models.AutoField(primary_key=True)
    cpf = models.CharField(unique=True, max_length=11)
    nome = models.CharField(max_length=100)
    dt_nascimento = models.DateField()

class AreaTecnologica(models.Model):
    id = models.AutoField(primary_key=True)
    area_tecnologica = models.CharField(max_length=100)
    
class Projeto(models.Model):
    id = models.AutoField(primary_key=True)
    projeto = models.CharField(max_length=100)    
    financiador = models.ForeignKey(Financiador, on_delete=models.CASCADE)
    area_tecnologica = models.ForeignKey(AreaTecnologica, on_delete=models.CASCADE)
    equipe = models.ManyToManyField(Colaborador)
    coordenador = models.TextField(max_length=100)
    ativo = models.BooleanField()
    inicio_vigencia = models.DateField()
    fim_vigencia = models.DateField()
    valor = models.DecimalField(max_digits=11, decimal_places=2)
    
    @property
    def qtd_membros(self):
        numero_membros = self.equipe.count()
        return numero_membros

    def qtd_membros_atualizada(self):
        self.qtd_membros = self.equipe.count()
        self.save()

    def inativar(self):
        self.ativo = False
        self.save()



