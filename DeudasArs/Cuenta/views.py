from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import login, authenticate

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            usuario = authenticate(rquest,
                                   usuario=cd['usuario'],
                                   password=cd['password'])
            if usuario is not None:
                if usuario.is_active:
                    login(request, usuario)
                    return render(request, 'usuario autenticado')
                else:
                    return render(request, 'usuario inactivo')
            else:
                return render(request, "información incorrecta")
        else:
            return render(request, "home.html", {'form': form})