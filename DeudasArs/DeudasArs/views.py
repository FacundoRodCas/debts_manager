from django.shortcuts import render
from Deudores.dolarjson import dolar_blue

def dolarblue(request):
    dolar = dolar_blue
    return render(request, "home.html", {"dolar": dolar})