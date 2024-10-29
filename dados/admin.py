from django.contrib import admin
from .models import Dados, Experiencia, Formacao

class ExperienciaInline(admin.TabularInline):
    model = Experiencia
    extra = 1  # Número de formulários de experiência adicionais a serem exibidos

class FormacaoInline(admin.TabularInline):
    model = Formacao
    extra = 1  # Número de formulários de formação adicionais a serem exibidos

@admin.register(Dados)
class DadosAdmin(admin.ModelAdmin):
    inlines = [ExperienciaInline, FormacaoInline]
    list_display = ('nome', 'email', 'telefone')  # Campos que deseja ver na lista principal