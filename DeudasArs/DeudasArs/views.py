from django.shortcuts import render
from Deudores.dolarjson import dolar_oficial

def dolaroficial(request):
    dolar = dolar_oficial
    return render(request, "home.html", {"dolar": dolar})