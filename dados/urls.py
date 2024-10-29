from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro_dados, name='formulario'),
    path('', views.index, name='index'),
]
