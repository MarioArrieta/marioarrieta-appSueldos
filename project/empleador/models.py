from django.db import models
from .choices import meses, liquidacion
from django.core.exceptions import ValidationError


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


# CLASE QUE PERMITE CREAR A UN EMPLEADO
class Empleado (models.Model):
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    cuil = models.PositiveIntegerField(validators=[validate_cuil_length], unique=True, verbose_name="CUIL")
    fecha_ingreso = models.DateField(verbose_name="Fecha de ingreso")
    fecha_baja = models.DateField(null= True, blank = True, verbose_name="Fecha de baja")
    email = models.EmailField(verbose_name= "e-Mail ")
    empleador = models.ForeignKey (Empleador, on_delete=models.CASCADE, verbose_name="Empleador")

    def __str__(self):
        return f"{self.apellido.title()}, {self.nombre.title()}"
    
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        

# CLASE QUE PERMITE CREAR PAGOS A EMPLEADOS
class Pagos (models.Model):
    fecha_notificacion = models.DateField(auto_now=True, verbose_name="Fecha de Notificación")
    fecha_pago = models.DateField(verbose_name="Fecha de Pago")
    importe = models.PositiveIntegerField(verbose_name="Importe")
    liquidacion = models.CharField(max_length=20, choices=liquidacion, verbose_name= "Liquidación")
    meses = models.CharField(max_length=10, choices=meses, verbose_name= "Mes")
    año = models.PositiveIntegerField(validators=[validate_year_range], verbose_name="Año")
    empleado = models.ForeignKey (Empleado, on_delete=models.CASCADE, verbose_name= "Empleado")
    archivo_adjunto = models.FileField (null=True, blank=True, upload_to="archivos/recibos/", verbose_name="Archivo adjunto")
    visto = models.BooleanField (editable=False, default=False, verbose_name="Visto")
    
    def __str__(self):
        return f"Pagos - {self.fecha_notificacion}"
    
    class Meta:
        verbose_name_plural = "Pagos"


# CLASE QUE PERMITE CREAR VACACIONES A EMPLEADOS
class Vacaciones (models.Model):
    fecha_notificacion = models.DateField(auto_now=True, verbose_name="Fecha de Notificación")
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de Finalizacion")
    período = models.PositiveIntegerField(validators=[validate_year_range], verbose_name="Corresponden al período")
    archivo_adjunto = models.FileField (null=True, blank=True, upload_to="archivos/vacaciones/", verbose_name="Archivo adjunto")
    visto = models.BooleanField (editable=False, default=False, verbose_name="Visto")
    empleado = models.ForeignKey (Empleado, on_delete=models.CASCADE, verbose_name= "Empleado")
    
    
    def __str__(self):
        return f"Vacaciones  - {self.fecha_notificacion}"
    
    class Meta:
        verbose_name_plural = "Vacaciones"

# CLASE QUE PERMITE CREAR SUSPENSIONES A EMPLEADOS
class Suspensiones (models.Model):
    fecha_notificacion = models.DateField(auto_now=True, verbose_name="Fecha de Notificación")
    cantidad_dias = models.PositiveIntegerField(verbose_name="Cantidad de días")
    fecha_reingreso = models.DateField(verbose_name="Fecha de Reingreso")
    motivo = models.CharField(max_length=200, verbose_name="Motivo")
    archivo_adjunto = models.FileField (null=True, blank=True, upload_to="archivos/suspensiones/", verbose_name="Archivo adjunto")
    visto = models.BooleanField (editable=False, default=False, verbose_name="Visto")
    empleado = models.ForeignKey (Empleado, on_delete=models.CASCADE, verbose_name= "Empleado")
    
    
    def __str__(self):
        return f"Suspensiones  - {self.fecha_notificacion}"
    
    class Meta:
        verbose_name_plural = "Suspensiones"
