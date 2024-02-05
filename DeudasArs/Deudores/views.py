from django.shortcuts import render, redirect
from .models import Deudores
from .forms import FormularioDeudores
from .dolarjson import dolar_blue

def mostrar_deudores(request):
    deudores = Deudores.objects.filter()
    return render(request, "deudores.html", {'deudores': deudores})

def crear_usuario(request):
    if request.method == 'POST':
        form = FormularioDeudores(request.POST)
        deuda_inicial_dolares = float(request.POST['deuda_inicial_pesos']) / dolar_blue
        if form.is_valid():
            deudor = form.save(commit=False)
            deudor.deuda_inicial_dolares = deuda_inicial_dolares
            deudor.deuda_actualizada_pesos = deuda_inicial_dolares * dolar_blue
            form.save()
            return redirect('deudores:')
        else:
            return redirect('deudores:')
    else:
        form = FormularioDeudores()
        return render(request, "crearusuario.html", {'form': form})
