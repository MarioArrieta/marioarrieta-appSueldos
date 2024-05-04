from django.shortcuts import render
from . import forms, models
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView
from empleador.models import Pagos, Vacaciones


def login (request):
    return render (request, "empleado/login.html")


class PagosRead(ListView):
    template_name = "empleado/index.html"

    def get_queryset(self):
        return Pagos.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacaciones'] = Vacaciones.objects.all()
        return context
    
    
class NotificacionesCreate(CreateView):
    model = models.Notificaciones
    form_class = forms.NotificacionesForm
    success_url = reverse_lazy ("empleado:index")


class PagosDetail (DetailView):
    model = Pagos
    template_name = "empleado/pagos_detail.html" 
    

class VacacionesDetail (DetailView):
    model = Vacaciones
    template_name = "empleado/vacaciones_detail.html"

