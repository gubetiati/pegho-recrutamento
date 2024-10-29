from django import forms
from .models import Dados

class DadosForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = ['nome', 'data_nascimento', 'email', 'telefone', 'endereco',
                  'cargo', 'empresa', 'periodo_experiencia', 'descricao_atividades',
                  'instituicao', 'curso', 'periodo_formacao']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: João da Silva'
            }),
            'data_nascimento': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'DD/MM/AAAA'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'exemplo@dominio.com'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: (99) 99999-9999'
            }),
            'endereco': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Rua Exemplo, 123'
            }),
            'cargo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Desenvolvedor'
            }),
            'empresa': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Empresa XYZ'
            }),
            'periodo_experiencia': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Jan 2020 - Dez 2021'
            }),
            'descricao_atividades': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descreva suas atividades...'
            }),
            'instituicao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Universidade XYZ'
            }),
            'curso': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Ciências da Computação'
            }),
            'periodo_formacao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 2018 - 2022'
            }),
        }
