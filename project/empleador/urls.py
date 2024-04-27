from django.urls import path
from empleador import views

app_name = "empleador"
urlpatterns = [
   
    path ("inicio/", views.inicio, name = "index"),
        path("empleador/create/", views.empleador_create, name="empleador_create"),
        path("empleado/create/", views.empleado_create, name="empleado_create"),
        path("pagos/create/", views.pagos_create, name="pagos_create"),
        path("vacaciones/create/", views.vacaciones_create, name="vacaciones_create"),
    

]