from django import forms

from . import models


class EmpleadorForm(forms.ModelForm):
    class Meta:
        model = models.Empleador
        fields = "__all__"

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = models.Empleado
        fields = "__all__"

class PagosForm(forms.ModelForm):
    class Meta:
        model = models.Pagos
        fields = "__all__"
        
class VacacionesForm(forms.ModelForm):
    class Meta:
        model = models.Vacaciones
        fields = "__all__"
