from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            usuario = authenticate(request,
                                   usuario=cd['usuario'],
                                   password=cd['password'])
            if usuario is not None:
                if usuario.is_active:
                    login(request, usuario)
                    return render(request, 'home.html')
                else:
                    return render(request, 'home.html')
            else:
                return render(request, "home.html")
    else:
        form = LoginForm()
        return render(request, "login.html", {'form': form})

def user_logout(request):
    return render(request, 'logout.html')

@login_required
def dashboard(request):
    return render(request,
                  'cuenta/dashboard.html')