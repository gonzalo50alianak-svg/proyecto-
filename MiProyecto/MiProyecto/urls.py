"""
URL configuration for MiProyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('App1.urls')),
]

from django.urls import path
from . import views

urlpatterns = [
    # --- RUTAS PARA USUARIOS ---
    # Muestra la lista de usuarios (usuarios.html)
    path('usuarios/', views.lista_usuarios, name='usuarios'),
    
    # Muestra el formulario y procesa el guardado (crear_usuarios.html)
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    
    # --- RUTAS PARA DETALLES DE VENTAS ---
    # Muestra la lista de detalles de venta (ventas_detalles.html)
    path('ventas-detalles/', views.lista_ventas_detalles, name='ventas_detalles'),
    
    # Muestra el formulario y procesa el guardado (crear_ventas_detalles.html)
    path('ventas-detalles/crear/', views.crear_venta_detalle, name='crear_venta_detalle'),
]
