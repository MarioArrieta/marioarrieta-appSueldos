from django.db import models

# Create your models here.

class Empleador (models.Model):
    razonSocial = models.CharField(max_length=20, verbose_name="Razon Social ")
    cuit = models.IntegerField(unique=True, verbose_name="CUIT ")
    email = models.EmailField(verbose_name="e-Mail ")
        
    def __str__(self):
        return self.razonSocial
    
    class Meta:
        verbose_name = "Empleador"
        verbose_name_plural = "Empleadores"



class Empleado (models.Model):
    apellido = models.CharField(max_length=20, verbose_name="Apellido ")
    nombre = models.CharField(max_length=20, verbose_name="Nombre ")
    cuil = models.IntegerField(unique=True, verbose_name="CUIT ")
    fecha_ingreso = models.DateField(verbose_name="Fecha de ingreso ")
    email = models.EmailField(verbose_name= "e-Mail ")
    empleador = models.ForeignKey (Empleador, on_delete=models.CASCADE, verbose_name="Empleador ")

    def __str__(self):
        return f"{self.apellido.upper()} ({self.empleador.razonSocial.title()})"
    
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        

    
class Pagos (models.Model):
    fecha_pago = models.DateField(verbose_name="Fecha de Pago ")
    importe = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Importe ")
    mensaje = models.CharField(max_length=50, verbose_name="Mensaje ")
    empleado = models.ForeignKey (Empleado, on_delete=models.CASCADE, verbose_name= "Empleado ")
    
    def __str__(self):
        return f" {self.empleado.apellido}, {self.empleado.nombre} - {self.fecha_pago}"
    
    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"

        
    
class Vacaciones (models.Model):
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio ")
    fecha_fin = models.DateField(verbose_name="Fecha de Finalizacion ")
    mensaje = models.CharField(max_length=50, verbose_name= "Mensaje ")
    empleado = models.ForeignKey (Empleado, on_delete=models.CASCADE, verbose_name= "Empleado ")
    
    def __str__(self):
        return f" {self.empleado.apellido}, {self.empleado.nombre}"
    
    class Meta:
        verbose_name_plural = "Vacaciones"
        