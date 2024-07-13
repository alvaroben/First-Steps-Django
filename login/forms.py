from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.translation import gettext_lazy as _


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Nombre de Usuario", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nombre de Usuario'}))
    password = forms.CharField(label="Contraseña",
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
