from django import forms
from .models import Novedad

class FormNovedad(forms.ModelForm):
    class Meta:
        model=Novedad
        fields="__all__"
        widgets={"created":forms.DateInput(attrs={'type':'date'})}
        widget=forms.Textarea(attrs={
            'placeholder': 'Escribe tu mensaje aquí...',
            'class': 'form-control',  # Opcional: añadir clases de Bootstrap
            'rows': 4  # Opcional: ajustar el número de filas
        })
