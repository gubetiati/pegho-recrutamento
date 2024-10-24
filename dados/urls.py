from django.urls import path
from .views import index, cadastro_dados  # Importa a view 'index'

# urlpatterns = [
#     path('', index, name='index'),  # Rota para a página inicial
# ]

urlpatterns = [
    path('cadastro/', cadastro_dados, name='cadastro'),
]
