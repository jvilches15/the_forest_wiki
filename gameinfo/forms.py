from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroFormulario(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control bg-dark-x border-0',
        'placeholder': 'Nombre de usuario',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control bg-dark-x border-0',
        'placeholder': 'Ingrese su contraseña',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control bg-dark-x border-0',
        'placeholder': 'Vuelva a ingresar su contraseña',
    }))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']