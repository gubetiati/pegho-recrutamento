from django import forms
from .models import Dados

class DadosForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = ['nome', 'data_nascimento', 'email', 'telefone', 'endereco',
                  'cargo', 'empresa', 'periodo_experiencia', 'descricao_atividades',
                  'instituicao', 'curso', 'periodo_formacao']