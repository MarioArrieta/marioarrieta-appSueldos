from . import forms, models
from empleado.models import Notificaciones, Empleado
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login



# Visualizacion de Inicio de Sesion
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "empleador/login.html"


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
            return redirect('empleador:login')

    else:
        form = CustomUserCreationForm()
    return render(request, "empleador/register.html", {"form": form})


# Abre el indice del Portal Empleador y muestras la notificaciones recibidas
class NotificacionesRead(LoginRequiredMixin, ListView):
    model = Notificaciones
    template_name = "empleador/index.html"
    login_url = reverse_lazy ("empleador:login")
    

# Muestra todos los empleados registrados    
class EmpleadoRead(LoginRequiredMixin, ListView):
    model = Empleado
    template_name = "empleador/empleado_buscar.html"
    login_url = reverse_lazy ("empleador:login")


# Muestra todos los empleados registrados    
class EmpleadorRead(LoginRequiredMixin, ListView):
    model = models.Empleador
    template_name = "empleador/empleador_buscar.html"
    login_url = reverse_lazy ("empleador:login")


# Muestra un detalle de las notificaciones recibidas por el empleador
class NotificacionesDetail(LoginRequiredMixin, DetailView):
    model = Notificaciones
    template_name = "empleador/notificaciones_detail.html"
    login_url = reverse_lazy ("empleador:login")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.visto = True
        obj.save()
        return obj

    

# Formulario para editar datos de los  empleados 
class EmpleadoUpdate(LoginRequiredMixin, UpdateView):
    model = models. Empleado
    form_class = forms.EmpleadoForm
    template_name = "empleador/empleado_update.html"
    success_url = reverse_lazy ("empleador:empleado_buscar")
    login_url = reverse_lazy ("empleador:login")


# Formulario para editar datos de los  empleados 
class EmpleadorUpdate(LoginRequiredMixin, UpdateView):
    model = models. Empleador
    form_class = forms.EmpleadorForm
    template_name = "empleador/empleador_update.html"
    success_url = reverse_lazy ("empleador:empleador_buscar")
    login_url = reverse_lazy ("empleador:login")


    
# Formulario para cargar empleadores
class EmpleadorCreate(LoginRequiredMixin, CreateView):
    model = models. Empleador
    form_class = forms.EmpleadorForm
    success_url = reverse_lazy ("empleador:empleador_buscar")
    login_url = reverse_lazy ("empleador:login")
    

# Formulario para cargar empleados 
class EmpleadoCreate(LoginRequiredMixin, CreateView):
    model = models. Empleado
    form_class = forms.EmpleadoForm
    success_url = reverse_lazy ("empleador:empleado_buscar")
    login_url = reverse_lazy ("empleador:login")


# Formulario para cargar pagos a los empleados
class PagosCreate(LoginRequiredMixin, CreateView):
    model = models.Pagos
    form_class = forms.PagosForm
    success_url = reverse_lazy ("empleador:empleado_buscar")
    login_url = reverse_lazy ("empleador:login")
    


# Formulario para cargar suspensiones a los empleados
class SuspensionesCreate(LoginRequiredMixin, CreateView):
    model = models.Suspensiones
    form_class = forms.SuspensionesForm
    success_url = reverse_lazy ("empleador:empleado_buscar")
    login_url = reverse_lazy ("empleador:login")


# Formulario para cargar vacaciones a los empleados
class VacacionesCreate (LoginRequiredMixin, CreateView):
    model = models.Vacaciones
    form_class = forms.VacacionesForm
    success_url = reverse_lazy ("empleador:empleado_buscar")
    login_url = reverse_lazy ("empleador:login")

# Elimina el registro de un empleado
class EmpleadoDelete(LoginRequiredMixin, DeleteView):
    model = models.Empleado
    success_url = reverse_lazy("empleador:empleado_buscar")
    login_url = reverse_lazy ("empleador:login")

# Elimina el registro de un empleado
class EmpleadorDelete(LoginRequiredMixin, DeleteView):
    model = models.Empleador
    success_url = reverse_lazy("empleador:empleador_buscar")
    login_url = reverse_lazy ("empleador:login")

