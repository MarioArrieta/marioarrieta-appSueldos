from django.urls import path
from empleado import views

app_name = "empleado"
urlpatterns = [
   
    path ("inicio/", views.inicio, name = "index"),
    path ("buscar/", views.buscar, name = "buscar"),
    path("pagos/read/", views.pagos_read, name="pagos_read"),
    path("vacaciones/read/", views.vacaciones_read, name="vacaciones_read"),
    
    
    

]