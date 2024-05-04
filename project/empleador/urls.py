from django.urls import path
from empleador import views

app_name = "empleador"
urlpatterns = [
   
        path ("inicio/", views.NotificacionesRead.as_view(), name = "index"),
        path ("login/", views.login, name = "login"),
        path("empleador/create/", views.EmpleadorCreate.as_view(), name="empleador_create"),
        path("empleado/create/", views.EmpleadoCreate.as_view(), name="empleado_create"),
        path("pagos/create/", views.PagosCreate.as_view(), name="pagos_create"),
        path("suspensiones/create/", views.SuspensionesCreate.as_view(), name="suspensiones_create"),
        path("vacaciones/create/", views.VacacionesCreate.as_view(), name="vacaciones_create"),
        
    

]