from django.shortcuts import render
from django.http import HttpResponse
from empleador.models import Vacaciones, Pagos

# Create your views here.

def inicio (request):
    return render (request, "empleado/index.html")

def buscar (request):
    return render (request, "empleado/buscar.html")

def pagos_read(request):
    if request.method == 'GET':
        cuil = request.GET.get('cuil')
        if cuil:
            pagos = Pagos.objects.filter(empleado__cuil=cuil)
            return render(request, 'empleado/pagos_read.html', {'pagos': pagos})
    return render(request, 'empleado/pagos_read.html', {})

def vacaciones_read(request):
    if request.method == 'GET':
        cuil = request.GET.get('cuil')
        if cuil:
            vacaciones = Vacaciones.objects.filter(empleado__cuil=cuil)
            return render(request, 'empleado/vacaciones_read.html', {'vacaciones': vacaciones})
    return render(request, 'empleado/vacaciones_read.html', {})


