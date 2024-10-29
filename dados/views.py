from django.shortcuts import render, redirect
from .forms import DadosForm

def index(request):
    return render(request, 'index.html')

def cadastro_dados(request):
    if request.method == 'POST':
        form = DadosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)  # Para debugar os erros do formulário
    else:
        form = DadosForm()
    return render(request, 'formulario.html', {'form': form})

