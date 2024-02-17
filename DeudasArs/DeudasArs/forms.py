from django import forms


class LoginForm(forms.Form):
    usuario = forms.CharField()
    password = forms.Charfield(widget=forms.PasswordInput)
