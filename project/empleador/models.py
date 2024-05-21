from django.db import models
from .choices import meses, liquidacion
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


# FUNCION QUE PERMITE VALIDAR AÑOS PARA QUE SE PUEDAD CARGAR ENTRE 1900 Y 2100
def validate_year_range(value):
    if value < 1900 or value > 2100:
        raise ValidationError("El año debe estar entre 1900 y 2100")
    

# FUNCION QUE ME PERMITE VALIDAR QUE UN CUIL TENGA 11 CARACTERES
def validate_cuil_length(value):
    cuil_length = len(str(value))
    if cuil_length != 11:
        raise ValidationError(f'El CUIL debe tener 11 dígitos')


# CLASE QUE PERMITE CREAR A UN EMPLEADOR
class Empleador (models.Model):
    razonSocial = models.CharField(max_length=50, verbose_name="Razon Social")
    cuit = models.PositiveIntegerField(validators=[validate_cuil_length], unique=True, verbose_name="CUIT")
    email = models.EmailField(verbose_name="e-Mail")

    def __str__(self):
        return f"{self.razonSocial.title()}"
    
    class Meta:
        verbose_name = "Empleador"
        verbose_name_plural = "Empleadores"

# CLASE QUE PERMITE AGREGAR UNA FOTO DE PERFIL AL USUARIO EMPLEADOR
class Avatar(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="avatar_empleador")
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return f"Foto de perfil de {self.usuario} "
    
    class Meta:
        verbose_name = "Foto de Perfil"
        verbose_name_plural = "Fotos de Perfiles"



# CLASE QUE PERMITE CREAR A UN EMPLEADO
class Empleado (models.Model):
    empleador = models.ForeignKey (Empleador, on_delete=models.CASCADE, verbose_name="Empleador")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    cuil = models.PositiveIntegerField(validators=[validate_cuil_length], unique=True, verbose_name="CUIL")
    fecha_ingreso = models.DateField(verbose_name="Fecha de ingreso")
    email = models.EmailField(verbose_name= "e-Mail ")
    
    
    def __str__(self):
        return f"{self.apellido.title()}, {self.nombre.title()} ({self.empleador.razonSocial.title()})"
    
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        

# CLASE QUE PERMITE CREAR PAGOS A EMPLEADOS
class Pagos (models.Model):
    empleado = models.ForeignKey (Empleado, on_delete=models.CASCADE, verbose_name= "Empleado")
    fecha_notificacion = models.DateField(auto_now=True, verbose_name="Fecha de Notificación", editable=False)
    fecha_pago = models.DateField(verbose_name="Fecha de Pago")
    importe = models.PositiveIntegerField(verbose_name="Importe")
    liquidacion = models.CharField(max_length=20, choices=liquidacion, verbose_name= "Liquidación")
    meses = models.CharField(max_length=10, choices=meses, verbose_name= "Mes",)
    año = models.PositiveIntegerField(validators=[validate_year_range], verbose_name="Año")
    imagen = models.ImageField(upload_to="pagos", null=True, blank=True)
    visto = models.BooleanField (editable=False, default=False, verbose_name="Visto")
    
    
    
    def __str__(self):
        return f"{self.fecha_notificacion} -  {self.empleado.apellido}, {self.empleado.nombre} ({self.empleado.empleador.razonSocial})"
    
    class Meta:
        verbose_name_plural = "Pagos"


# CLASE QUE PERMITE CREAR VACACIONES A EMPLEADOS
class Vacaciones (models.Model):
    empleado = models.ForeignKey (Empleado, on_delete=models.CASCADE, verbose_name= "Empleado")
    fecha_notificacion = models.DateField(auto_now=True, verbose_name="Fecha de Notificación", editable=False)
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de Finalizacion")
    período = models.PositiveIntegerField(validators=[validate_year_range], verbose_name="Corresponden al año")
    imagen = models.ImageField(upload_to="vacaciones", null=True, blank=True)
    visto = models.BooleanField (editable=False, default=False, verbose_name="Visto")
    
    
    
    
    def __str__(self):
        return f"{self.fecha_notificacion} - {self.empleado.apellido}, {self.empleado.nombre} ({self.empleado.empleador.razonSocial})"
    
    class Meta:
        verbose_name_plural = "Vacaciones"

# CLASE QUE PERMITE CREAR SUSPENSIONES A EMPLEADOS
class Suspensiones (models.Model):
    empleado = models.ForeignKey (Empleado, on_delete=models.CASCADE, verbose_name= "Empleado")
    fecha_notificacion = models.DateField(auto_now=True, verbose_name="Fecha de Notificación", editable=False)
    cantidad_dias = models.PositiveIntegerField(verbose_name="Cantidad de días")
    fecha_reingreso = models.DateField(verbose_name="Fecha de Reingreso")
    motivo = models.CharField(max_length=200, verbose_name="Motivo")
    imagen = models.ImageField(upload_to="suspensiones", null=True, blank=True)
    visto = models.BooleanField (editable=False, default=False, verbose_name="Visto")
    
    
    
    def __str__(self):
        return f"{self.fecha_notificacion} - {self.empleado.apellido}, {self.empleado.nombre} ({self.empleado.empleador.razonSocial})"
    
    class Meta:
        verbose_name_plural = "Suspensiones"
