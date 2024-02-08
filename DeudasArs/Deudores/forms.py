from django import forms
from django.forms import ModelForm
from .models import Deudores


class FormularioDeudores(ModelForm):
    class Meta:
        model = Deudores
        fields = ['nombre', 'apellido', 'deuda_inicial_pesos', 'intereses_mensuales']