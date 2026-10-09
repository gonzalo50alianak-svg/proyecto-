# Importamos el módulo 'forms' de Django
from django import forms
# Importamos el modelo que creamos anteriormente
from .models import AutoMercedes

class AutoMercedesForm(forms.ModelForm):
    """
    Formulario basado en el modelo AutoMercedes para crear o editar registros.
    """
    class Meta:
        # Indicamos qué modelo utilizará este formulario
        model = AutoMercedes
        
        # Indicamos qué campos del modelo se incluirán en el formulario
        fields = ['nombre', 'clase', 'anio', 'precio', 'disponible']
        
        # Agregamos estilos CSS básicos (como Bootstrap) a los campos
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. C 300 Sedan'}),
            'clase': forms.Select(attrs={'class': 'form-select'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '2024'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 55000.00'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }