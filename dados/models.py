from django.db import models

class Dados(models.Model):
    # Dados Pessoais
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()

    # Contato
    email = models.EmailField(max_length=100, unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()

    # Experiência Profissional
    cargo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    periodo_experiencia = models.CharField(max_length=50)  # Ex: "Jan/2020 - Dez/2021"
    descricao_atividades = models.TextField()

    # Formação Acadêmica
    instituicao = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    periodo_formacao = models.CharField(max_length=50)  # Ex: "2018 - 2022"

    def __str__(self):
        return self.nome
