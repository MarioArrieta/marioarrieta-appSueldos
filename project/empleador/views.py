from . import forms, models
from empleado.models import Notificaciones
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect




class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "empleador/login.html"


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleador:login')

    else:
        form = CustomUserCreationForm()
    return render(request, "empleador/empleador_form.html", {"form": form})


class NotificacionesRead(LoginRequiredMixin,ListView):
    model = Notificaciones
    template_name = "empleador/index.html"
   

# class EmpleadorCreate(LoginRequiredMixin, CreateView):
#     model = models.Empleador
#     form_class = forms.EmpleadorForm
#     success_url = reverse_lazy ("empleador:login")


class EmpleadoCreate(LoginRequiredMixin, CreateView):
    model = models. Empleado
    form_class = forms.EmpleadoForm
    success_url = reverse_lazy ("empleador:index")


class PagosCreate(LoginRequiredMixin, CreateView):
    model = models.Pagos
    form_class = forms.PagosForm
    success_url = reverse_lazy ("empleador:index")


class SuspensionesCreate(LoginRequiredMixin,CreateView):
    model = models.Suspensiones
    form_class = forms.SuspensionesForm
    success_url = reverse_lazy ("empleador:index")


class VacacionesCreate (LoginRequiredMixin, CreateView):
    model = models.Vacaciones
    form_class = forms.VacacionesForm
    success_url = reverse_lazy ("empleador:index")

