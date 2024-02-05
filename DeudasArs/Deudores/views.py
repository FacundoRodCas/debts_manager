from django.shortcuts import render
from .models import Deudores
from .forms import FormuarioDeudores

def mostrar_deudores(request):
    deudores = Deudores.objects.filter()
    return render(request, "deudores.html", {'deudores': deudores})
