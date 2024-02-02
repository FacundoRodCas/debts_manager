from django.shortcuts import render

def mostrar_deudores(request):
    return render(request, "deudores.html")
