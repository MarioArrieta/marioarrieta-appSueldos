from django.urls import path
from empleador import views
from django.contrib.auth.views import LogoutView

app_name = "empleador"
urlpatterns = [
   
        path ("login/", views.CustomLoginView.as_view(), name = "login"),
        path ("inicio/", views.NotificacionesRead.as_view(), name = "index"),
        path ("register/", views.register, name="register"),
        path ("logout/", LogoutView.as_view(template_name="empleador/logout.html"), name="logout"),
        path ("empleado/buscar/", views.EmpleadoRead.as_view(), name = "empleado_buscar"),
        path ("notificaciones/detail/<pk>", views.NotificacionesDetail.as_view(), name ="notificaciones_detail"),
        path("empleador/create/", views.EmpleadorCreate.as_view(), name="empleador_create"),
        path("empleado/create/", views.EmpleadoCreate.as_view(), name="empleado_create"),
        path("pagos/create/", views.PagosCreate.as_view(), name="pagos_create"),
        path("suspensiones/create/", views.SuspensionesCreate.as_view(), name="suspensiones_create"),
        path("vacaciones/create/", views.VacacionesCreate.as_view(), name="vacaciones_create"),
        
    

]