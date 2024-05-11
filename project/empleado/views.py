from django.shortcuts import render
from . import forms, models
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView
from empleador.models import Pagos, Vacaciones, Suspensiones
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect



# Visualizacion de Inicio de Sesion
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "empleado/login.html"


# Formulario para crear un usuario
def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleado:login')

    else:
        form = CustomUserCreationForm()
    return render(request, "empleado/register.html", {"form": form})


# Abre el indice del Portal Empleado y muestras la notificaciones recibidas
class PagosRead(LoginRequiredMixin, ListView):
    template_name = "empleado/index.html"
    def get_queryset(self):
        return Pagos.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['suspensiones'] = Suspensiones.objects.all()
        context['vacaciones'] = Vacaciones.objects.all()
        return context
    

# Formulario para cargar notificaciones    
class NotificacionesCreate(LoginRequiredMixin, CreateView):
    model = models.Notificaciones
    form_class = forms.NotificacionesForm
    success_url = reverse_lazy ("empleado:index")


# Muestra un detalle de las notificaciones (Pagos) recibidas por el empleador
class PagosDetail (LoginRequiredMixin, DetailView):
    model = Pagos
    template_name = "empleado/pagos_detail.html" 
    

# Muestra un detalle de las notificaciones (Vacaciones) recibidas por el empleador
class VacacionesDetail (LoginRequiredMixin, DetailView):
    model = Vacaciones
    template_name = "empleado/vacaciones_detail.html"

# Muestra un detalle de las notificaciones (Vacaciones) recibidas por el empleador
class SuspensionesDetail (LoginRequiredMixin, DetailView):
    model = Suspensiones
    template_name = "empleado/suspensiones_detail.html"

