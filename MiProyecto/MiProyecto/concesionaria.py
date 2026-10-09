INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Mis Aplicaciones
    'cliente',
    'administrador',
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Ruta principal (Landing pública del cliente)
    path('', include('cliente.urls')),
    
    # Ruta de gestión interna (Panel de administración)
    path('gestion/', include('administrador.urls')),
]