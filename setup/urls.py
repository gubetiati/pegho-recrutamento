from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dados.urls')),  # Inclui as URLs da aplicação 'dados'
]
