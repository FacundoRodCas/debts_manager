from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    usuario = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=20, label="Nombre de usuario")
    firstname = forms.CharField(max_length=20, label="Nombre")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Repite la contraseña")
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ['username', 'firstname', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            return forms.ValidationError('Las contraseñas no coinciden')
        return cd['password2']
