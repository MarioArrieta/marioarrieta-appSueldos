from django.shortcuts import render
from . import forms, models
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from empleador.models import Pagos, Vacaciones, Suspensiones
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login



# Visualizacion de Inicio de Sesion
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "empleado/login.html"


# Formulario para crear un usuario
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            if 'avatar' in request.FILES:
                avatar = models.Avatar(usuario=user, avatar=request.FILES['avatar'])
                avatar.save()
            login(request, user)
            return redirect('empleado:login')

    else:
        form = CustomUserCreationForm()
    return render(request, "empleado/register.html", {"form": form})


# Abre el indice del Portal Empleado y muestras la notificaciones recibidas
class PagosRead(LoginRequiredMixin, ListView):
    template_name = "empleado/index.html"
    login_url = reverse_lazy ("empleado:login")
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
    login_url = reverse_lazy ("empleado:login")


# Muestra un detalle de las notificaciones (Pagos) recibidas por el empleador
class PagosDetail (LoginRequiredMixin, DetailView):
    model = Pagos
    template_name = "empleado/pagos_detail.html" 
    login_url = reverse_lazy ("empleado:login")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.visto = True
        obj.save()
        return obj

    

# Muestra un detalle de las notificaciones (Vacaciones) recibidas por el empleador
class VacacionesDetail (LoginRequiredMixin, DetailView):
    model = Vacaciones
    template_name = "empleado/vacaciones_detail.html"
    login_url = reverse_lazy ("empleado:login")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.visto = True
        obj.save()
        return obj


# Muestra un detalle de las notificaciones (Vacaciones) recibidas por el empleador
class SuspensionesDetail (LoginRequiredMixin, DetailView):
    model = Suspensiones
    template_name = "empleado/suspensiones_detail.html"
    login_url = reverse_lazy ("empleado:login")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.visto = True
        obj.save()
        return obj


