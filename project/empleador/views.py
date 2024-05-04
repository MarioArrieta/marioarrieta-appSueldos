from django.shortcuts import render
from . import forms, models
from empleado.models import Notificaciones
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView


def inicio (request):
    return render (request, "empleador/index.html")


def login (request):
    return render (request, "empleador/login.html")


class NotificacionesRead(ListView):
    model = Notificaciones
    template_name = "empleador/index.html"
   

class EmpleadorCreate(CreateView):
    model = models.Empleador
    form_class = forms.EmpleadorForm
    success_url = reverse_lazy ("empleador:login")


class EmpleadoCreate(CreateView):
    model = models. Empleado
    form_class = forms.EmpleadoForm
    success_url = reverse_lazy ("empleador:index")


class PagosCreate(CreateView):
    model = models.Pagos
    form_class = forms.PagosForm
    success_url = reverse_lazy ("empleador:index")


class SuspensionesCreate(CreateView):
    model = models.Suspensiones
    form_class = forms.SuspensionesForm
    success_url = reverse_lazy ("empleador:index")


class VacacionesCreate (CreateView):
    model = models.Vacaciones
    form_class = forms.VacacionesForm
    success_url = reverse_lazy ("empleador:index")

