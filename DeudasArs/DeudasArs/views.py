from django.shortcuts import render
from .dolarjson

def dolarblue(request):
    dolar = dolar_blue
    return render(request, "home.html", {"dolar": dolar})