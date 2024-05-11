from . import forms, models
from empleado.models import Notificaciones, Empleado
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect




# Visualizacion de Inicio de Sesion
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "empleador/login.html"


# Formulario para crear un usuario
def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleador:login')

    else:
        form = CustomUserCreationForm()
    return render(request, "empleador/register.html", {"form": form})


class NotificacionesRead(LoginRequiredMixin, ListView):
    model = Notificaciones
    template_name = "empleador/index.html"


class EmpleadoRead(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    model = Empleado
    template_name = "empleador/empleado_buscar.html"


# Formulario para cargar empleadores
class EmpleadorCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models. Empleador
    form_class = forms.EmpleadorForm
    success_url = reverse_lazy ("empleador:index")
    

# Formulario para cargar empleados 
class EmpleadoCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models. Empleado
    form_class = forms.EmpleadoForm
    success_url = reverse_lazy ("empleador:index")


# Formulario para cargar pagos a los empleados
class PagosCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Pagos
    form_class = forms.PagosForm
    success_url = reverse_lazy ("empleador:index")


# Formulario para cargar suspensiones a los empleados
class SuspensionesCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = models.Suspensiones
    form_class = forms.SuspensionesForm
    success_url = reverse_lazy ("empleador:index")


# Formulario para cargar vacaciones a los empleados
class VacacionesCreate (LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Vacaciones
    form_class = forms.VacacionesForm
    success_url = reverse_lazy ("empleador:index")

