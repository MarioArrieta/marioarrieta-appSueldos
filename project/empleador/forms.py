from django import forms
from django.db import models
from empleador.models import Empleado, Pagos, Vacaciones, Suspensiones
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su CUIT'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))

    class Meta:
        model = User
        fields = ["username", "password"]


class CustomUserCreationForm(UserCreationForm):
    razon_social = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    usuario = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su CUIT'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_usuario(self):
        usuario = self.cleaned_data['usuario']
        if not usuario.isdigit() or len(usuario) != 11:
            raise ValidationError('El CUIT debe tener 11 caracteres numéricos.')
        return usuario

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['usuario']
        user.last_name = self.cleaned_data['razon_social']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ["razon_social", "email", "usuario", "password1", "password2" ]


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = "__all__"

class PagosForm(forms.ModelForm):
    class Meta:
        model = Pagos
        fields = "__all__"
        
class VacacionesForm(forms.ModelForm):
    class Meta:
        model = Vacaciones
        fields = "__all__"

class SuspensionesForm(forms.ModelForm):
    class Meta:
        model = Suspensiones
        fields = "__all__"

