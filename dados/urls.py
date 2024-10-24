from django.urls import path
from .views import index  # Importa a view 'index'

urlpatterns = [
    path('', index, name='index'),  # Rota para a página inicial
]
