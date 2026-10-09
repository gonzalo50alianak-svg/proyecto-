from django.shortcuts import render
from .models import *

# Create your views here.
def mostrar_index(request):

    return render(request, 'App1/index.html')

python
from django.urls import path
# Importamos las vistas desde el mismo directorio
from . import views

urlpatterns = [
    # Ruta para registrar un auto: http://127.0.0.1:8000/crear/
    path('crear/', views.crear_auto, name='crear_auto'),
    
    # Ruta para ver el catálogo: http://127.0.0.1:8000/
    path('', views.lista_autos, name='lista_autos'),
]

from django.shortcuts import render

def index_cliente(request):
    # Renderiza la landing page pública del cliente
    return render(request, 'cliente/index.html')