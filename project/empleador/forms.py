from django import forms
from empleador.models import Empleado, Empleador, Pagos, Vacaciones, Suspensiones
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su CUIT', 'autocomplete': 'new-password' }))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'autocomplete': 'new-password'}))

    class Meta:
        model = User
        fields = ["username", "password"]


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    avatar = forms.ImageField(label="Foto de Perfil",required=False)
 
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "avatar"]


class EmpleadorForm(forms.ModelForm):
    razonSocial = forms.CharField(label="Razon Social ", widget=forms.TextInput(attrs={'class': 'form-control'}))
    cuit = forms.CharField( label= "CUIT ", max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label= "e-mail", widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Empleador
        fields = "__all__"



class EmpleadoForm(forms.ModelForm):
    empleador = forms.ModelChoiceField(queryset=Empleador.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    apellido = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}))
    nombre = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}))
    cuil = forms.CharField(label="CUIL", max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha_ingreso = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    email = forms.CharField(label= "e-mail ", widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Empleado
        fields = "__all__"


class PagosForm(forms.ModelForm):
    empleado = forms.ModelChoiceField(queryset=Empleado.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    fecha_pago = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    importe = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}))
    año = forms.CharField( max_length=4, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Pagos
        fields = "__all__"

        
class VacacionesForm(forms.ModelForm):
    empleado = forms.ModelChoiceField(queryset=Empleado.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    fecha_fin = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    período = forms.CharField( max_length=4, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Vacaciones
        fields = "__all__"


class SuspensionesForm(forms.ModelForm):
    empleado = forms.ModelChoiceField(queryset=Empleado.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    cantidad_dias = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha_reingreso = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    motivo = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Suspensiones
        fields = "__all__"

