from django import forms


class FormuarioDeudores(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    fecha = forms.DateTimeField()
    deuda_inicial_pesos = forms.FloatField()
    deuda_inicial_dolares = forms.FloatField()
    deuda_actualizada_pesos = forms.FloatField()
    