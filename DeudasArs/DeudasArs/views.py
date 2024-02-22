from django.shortcuts import render


def dolarblue(request):
    dolar = dolar_blue
    return render(request, "home.html", {"dolar": dolar})