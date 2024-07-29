from django import forms
from .models import Herramientas,Acta_entrega_herramienta

class Form_Herramienta(forms.ModelForm):
    class Meta:
        model=Herramientas
        fields="__all__"
        widgets={"created":forms.DateInput(attrs={'type':'date'})}

class Form_Acta_trabajo(forms.ModelForm):
    class Meta:
        model=Acta_entrega_herramienta
        fields="__all__"
        widgets={"created": forms.DateInput(attrs={"type":"date"})}

