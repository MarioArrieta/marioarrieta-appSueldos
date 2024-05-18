from django.contrib import admin
from . import models

admin.site.register(models.Empleador)
admin.site.register(models.Empleado)
admin.site.register(models.Pagos)
admin.site.register(models.Vacaciones)
admin.site.register(models.Suspensiones)
admin.site.register(models.Avatar)

