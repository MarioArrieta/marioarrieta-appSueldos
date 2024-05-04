from django.urls import path
from empleado import views

app_name = "empleado"
urlpatterns = [
   
    path ("inicio/", views.PagosRead.as_view(), name = "index"),
    path ("login/", views.login, name = "login"),
    path("notificaciones/create", views.NotificacionesCreate.as_view(), name="notificaciones_create"),
    path("pagos/detail/<pk>", views.PagosDetail.as_view(), name="pagos_detail"),
    path("vacaciones/detail/<pk>", views.VacacionesDetail.as_view(), name="vacaciones_detail"),
 
]