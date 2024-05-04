from django.db import models
from empleador.models import Empleado
from .choices import tipo_notificacion



# CLASE QUE PERMITE CREAR NOTIFICACIONES DE LOS EMPLEADOS
class Notificaciones(models.Model):
    fecha_notificacion = models.DateField(auto_now=True, verbose_name="Fecha de Notificación")
    tipo = models.CharField(max_length=20, choices=tipo_notificacion, verbose_name= "Tipo")
    descripcion = models.CharField(null= True, blank=True, max_length=200, verbose_name="Descripcion")
    archivo_adjunto = models.FileField (null=True, blank=True, upload_to="archivos/recibos/", verbose_name="Archivo adjunto")
    visto = models.BooleanField (editable=False, default=False, verbose_name="Visto")
    empleado = models.ForeignKey (Empleado, on_delete=models.CASCADE, verbose_name= "Empleado")
    
    def __str__(self):
        return f"Notificaciones - {self.fecha_notificacion}"
    
    class Meta:
        verbose_name_plural = "Notificaciones"