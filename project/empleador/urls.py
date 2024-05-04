from django.urls import path
from empleador import views

app_name = "empleador"
urlpatterns = [
   
        path ("inicio/", views.inicio, name = "index"),
        path ("login/", views.login, name = "login"),
        path("empleador/create/", views.EmpleadorCreate.as_view(), name="empleador_create"),
        path("empleado/create/", views.EmpleadoCreate.as_view(), name="empleado_create"),
        path("pagos/create/", views.PagosCreate.as_view(), name="pagos_create"),
        path("vacaciones/create/", views.VacacionesCreate.as_view(), name="vacaciones_create"),
    

]