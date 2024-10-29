from django.shortcuts import render, redirect
from .forms import DadosForm, ExperienciaFormSet, FormacaoFormSet

def index(request):
    return render(request, 'index.html')

def cadastro_dados(request):
    if request.method == 'POST':
        dados_form = DadosForm(request.POST)
        if dados_form.is_valid():
            dados = dados_form.save()
            
            # Criação dos formsets com o objeto pai 'dados'
            experiencia_formset = ExperienciaFormSet(request.POST, instance=dados, prefix='experiencia')
            formacao_formset = FormacaoFormSet(request.POST, instance=dados, prefix='formacao')

            if experiencia_formset.is_valid() and formacao_formset.is_valid():
                experiencias = experiencia_formset.save(commit=False)
                for experiencia in experiencias:
                    experiencia.dados = dados
                    experiencia.save()

                formacoes = formacao_formset.save(commit=False)
                for formacao in formacoes:
                    formacao.dados = dados
                    formacao.save()
                
                return redirect('index')
    else:
        dados_form = DadosForm()
        experiencia_formset = ExperienciaFormSet(prefix='experiencia')
        formacao_formset = FormacaoFormSet(prefix='formacao')
    
    return render(request, 'formulario.html', {
        'dados_form': dados_form,
        'experiencia_formset': experiencia_formset,
        'formacao_formset': formacao_formset,
    })