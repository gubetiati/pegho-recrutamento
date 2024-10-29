from django import forms
from .models import Dados, Experiencia, Formacao

class DadosForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = ['nome', 'data_nascimento', 'email', 'telefone', 'endereco']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: João da Silva'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/AAAA'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'exemplo@dominio.com'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: (99) 99999-9999'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Rua Exemplo, 123'}),
        }

class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = ['cargo', 'empresa', 'periodo_experiencia']
        widgets = {
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'periodo_experiencia': forms.TextInput(attrs={'class': 'form-control'}),
        }

class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = ['instituicao', 'curso', 'periodo_formacao']
        widgets = {
            'instituicao': forms.TextInput(attrs={'class': 'form-control'}),
            'curso': forms.TextInput(attrs={'class': 'form-control'}),
            'periodo_formacao': forms.TextInput(attrs={'class': 'form-control'}),
        }

ExperienciaFormSet = forms.inlineformset_factory(Dados, Experiencia, form=ExperienciaForm, extra=1, can_delete=False)
FormacaoFormSet = forms.inlineformset_factory(Dados, Formacao, form=FormacaoForm, extra=1, can_delete=False)
