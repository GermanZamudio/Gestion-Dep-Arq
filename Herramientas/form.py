from django import forms
from .models import Herramientas, Acta_entrega_herramienta, Ubicacion

class Form_Herramienta(forms.ModelForm):
    class Meta:
        model = Herramientas
        fields = ['nombre', 'marca', 'ubicacion', 'Funcion']

    ubicacion = forms.ModelChoiceField(
        queryset=Ubicacion.objects.all(),
        widget=forms.Select(attrs={'class': 'select_ubicacion'}),
    )

class Form_Acta_trabajo(forms.ModelForm):
    class Meta:
        model = Acta_entrega_herramienta
        fields = ['Destino', 'Herramienta', 'Recibe', 'Entrega']

    Herramienta = forms.ModelMultipleChoiceField(
        queryset=Herramientas.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'select_herramienta'}),
    )