from django.urls import path
from empleador import views

 

app_name = "empleador"
urlpatterns = [
   
        path ("login/", views.CustomLoginView.as_view(), name = "login"),
        path ("inicio/", views.NotificacionesRead.as_view(), name = "index"),
        path ("register/", views.register, name="register"),
        path ("empleado/buscar/", views.EmpleadoRead.as_view(), name = "empleado_buscar"),
        path ("empleador/buscar/", views.EmpleadorRead.as_view(), name = "empleador_buscar"),
        path ("notificaciones/detail/<pk>", views.NotificacionesDetail.as_view(), name ="notificaciones_detail"),
        path ("empleado/update/<pk>", views.EmpleadoUpdate.as_view(), name ="empleado_update"),
        path ("empleador/update/<pk>", views.EmpleadorUpdate.as_view(), name ="empleador_update"),
        path("empleador/create/", views.EmpleadorCreate.as_view(), name="empleador_create"),
        path("empleado/create/", views.EmpleadoCreate.as_view(), name="empleado_create"),
        path("pagos/create/", views.PagosCreate.as_view(), name="pagos_create"),
        path("suspensiones/create/", views.SuspensionesCreate.as_view(), name="suspensiones_create"),
        path("vacaciones/create/", views.VacacionesCreate.as_view(), name="vacaciones_create"),
        path("empleado/delete/<int:pk>", views.EmpleadoDelete.as_view(), name="empleado_delete"),
        path("empleador/delete/<int:pk>", views.EmpleadorDelete.as_view(), name="empleador_delete"),
        
    

]

