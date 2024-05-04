from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView
from empleador import models


def login (request):
    return render (request, "empleado/login.html")


class PagosRead(ListView):
    template_name = "empleado/index.html"

    def get_queryset(self):
        return models.Pagos.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacaciones'] = models.Vacaciones.objects.all()
        return context


class PagosDetail (DetailView):
    model = models.Pagos
    template_name = "empleado/pagos_detail.html" 
    

class VacacionesDetail (DetailView):
    model = models.Vacaciones
    template_name = "empleado/vacaciones_detail.html"

