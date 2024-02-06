from django.shortcuts import render, redirect
from .models import Deudores
from .forms import FormularioDeudores
from .dolarjson import dolar_blue

def mostrar_deudores(request):
    if request.method == 'GET':
        deudores = Deudores.objects.filter()
        deudas_actualizadas = []
        for deudor in deudores:
            deuda_actualizada = deudor.deuda_inicial_dolares * dolar_blue
            deuda_actualizada = round(deuda_actualizada, 2)
            deudas_actualizadas.append(deuda_actualizada)
        return render(request, "deudores.html", {'deudores': deudores, 'deudas_actualizadas': deudas_actualizadas})

def crear_deuda(request):
    if request.method == 'POST':
        form = FormularioDeudores(request.POST)
        deuda_inicial_pesos = float(request.POST['deuda_inicial_pesos'])
        #usuario = request.POST['usuario']
        if form.is_valid():
            deudor = form.save(commit=False)
            #deudor.usuario = usuario
            deudor.deuda_inicial_dolares = deuda_inicial_pesos / dolar_blue
            form.save()
            return redirect('deudores:')
        else:
            return redirect('deudores:')
    else:
        form = FormularioDeudores()
        return render(request, "crearusuario.html", {'form': form})
