from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    usuario = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.Form):
    usuario = forms.CharField(max_length=20)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'firstname', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            return forms.ValidationError('Las contraseñas no coinciden')
        return cd['password2']