from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from empleador.models import Empleado


from . import models


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su CUIT', 'autocomplete': 'new-password'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'autocomplete': 'new-password'}))

    class Meta:
        model = User
        fields = ["username", "password"]


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class NotificacionesForm(forms.ModelForm):
    empleado = forms.ModelChoiceField(queryset=Empleado.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    descripcion = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    
    class Meta:
        model = models.Notificaciones
        fields = "__all__"
