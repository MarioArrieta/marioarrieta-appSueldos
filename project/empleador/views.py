
from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages

def inicio (request):
    return render (request, "empleador/index.html")

def empleador_create (request):
    if request.method == "POST":
        form = forms.EmpleadorForm (request.POST)
        try:
            if form.is_valid:
                form.save()
                return redirect ("empleador:index")
        except ValueError:
            messages.error (request,"")
    else:
        form = forms.EmpleadorForm()
    return render (request, "empleador/empleador_create.html", context={"form":form})


def empleado_create (request):
    if request.method == "POST":
        form = forms.EmpleadoForm (request.POST)
        try:
            if form.is_valid:
                form.save()
                return redirect ("empleador:index")
        except ValueError:
            messages.error (request,"")
    else:
        form = forms.EmpleadoForm()
    return render (request, "empleador/empleado_create.html", context={"form":form})


def pagos_create (request):
    if request.method == "POST":
        form = forms.PagosForm (request.POST)
        try:
            if form.is_valid:
                form.save()
                return redirect ("empleador:index")
        except ValueError:
            messages.error(request,"")
    else:
        form = forms.PagosForm()
    return render (request, "empleador/pagos_create.html", context={"form":form})


def vacaciones_create (request):
    if request.method == "POST":
        form = forms.VacacionesForm (request.POST)
        try:
            if form.is_valid:
                form.save()
                return redirect ("empleador:index")
        except ValueError:
            messages.error(request, "")
    else:
        form = forms.VacacionesForm()
    return render (request, "empleador/vacaciones_create.html", context={"form":form})







