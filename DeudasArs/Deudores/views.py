from django.shortcuts import render, redirect
from .models import Deudores
from .forms import FormularioDeudores
from .dolarjson import dolar_blue
from datetime import date

def mostrar_deudores(request):
    if request.method == 'GET':
        deudores = Deudores.objects.filter()
        deudas_actualizadas = []
        today = date.today()
        for deudor in deudores:
            meses = ((today.year - deudor.fecha.year) * 12) + (today.month - deudor.fecha.month)
            interes = (deudor.deuda_inicial_dolares / 100) * deudor.intereses_mensuales
            intereses_totales = interes * meses
            deuda_actualizada = (deudor.deuda_inicial_dolares + intereses_totales) * dolar_blue
            deudas_actualizadas.append(deuda_actualizada)
        deudas = zip(deudores, deudas_actualizadas)
        return render(request, "deudores.html", {'deudas': deudas})


def crear_deuda(request):
    if request.method == 'POST':
        form = FormularioDeudores(request.POST)
        deuda_inicial_pesos = float(request.POST['deuda_inicial_pesos'])
        #usuario = request.POST['usuario']
        if form.is_valid():
            deudor = form.save(commit=False)
            #deudor.usuario = usuario
            deudor.deuda_inicial_dolares = deuda_inicial_pesos / dolar_blue
            deudor.fecha = date.today()
            form.save()
            return redirect('deudores:')
        else:
            return redirect('deudores:')
    else:
        form = FormularioDeudores()
        return render(request, "crearusuario.html", {'form': form})


def modificar_deuda(request, pk):
    deuda = Deudores.objects.get(pk=pk)
    if request.method == 'POST':
        form = FormularioDeudores(request.POST, instance=deuda)
        if form.is_valid():
            deudor = form.save(commit=False)
            deudor.deuda_inicial_dolares = deudor.deuda_inicial_pesos / dolar_blue
            form.save()
            return redirect('deudores:')
    else:
        form = FormularioDeudores(instance=deuda)
    return render(request, "modificar.html", {'form': form})


def eliminar_deuda(request, pk):
    deuda = Deudores.objects.get(pk=pk)
    deuda.delete()
    return redirect('deudores:')
