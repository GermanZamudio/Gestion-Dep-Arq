from django import forms
from .models import (
    ArticuloUsoDiario,
    ArticuloLicitacion,
    MovimientoLicitacion,
    MovimientoUsoDiario,
    Utilidad
)


class FormArticuloLicitacion(forms.ModelForm):
    class Meta:
        model = ArticuloLicitacion
        fields = "__all__"
        widgets = {"created": forms.DateInput(attrs={"type": "date"})}


class FormArticulo(forms.ModelForm):
    class Meta:
        model = ArticuloUsoDiario
        fields = "__all__"
        widgets = {"created": forms.DateInput(attrs={"type": "date"})}


class FormMovimiento(forms.ModelForm):
    class Meta:
        model = MovimientoUsoDiario
        fields = "__all__"
        widgets = {"created": forms.DateInput(attrs={"type": "date"})}


class FormMovimientoLicitacion(forms.ModelForm):
    class Meta:
        model = MovimientoLicitacion
        fields = "__all__"
        widgets = {"created": forms.DateInput(attrs={"type": "date"})}



class FormUtilidad(forms.ModelForm):
    class Meta:
        model = Utilidad
        fields = "__all__"
        widgets = {"created": forms.DateInput(attrs={"type": "date"})}

