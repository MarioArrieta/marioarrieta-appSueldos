from django import forms

from . import models

class NotificacionesForm(forms.ModelForm):
    class Meta:
        model = models.Notificaciones
        fields = "__all__"
