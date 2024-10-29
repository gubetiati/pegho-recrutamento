from django.db import models

class Dados(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    

class Experiencia(models.Model):
    dados = models.ForeignKey(Dados, on_delete=models.CASCADE, related_name='experiencias')
    cargo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    periodo_experiencia = models.CharField(max_length=100)

class Formacao(models.Model):
    dados = models.ForeignKey(Dados, on_delete=models.CASCADE, related_name='formacoes')
    instituicao = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    periodo_formacao = models.CharField(max_length=100)
