from django.urls import path
from empleado import views
from django.contrib.auth.views import LogoutView

app_name = "empleado"
urlpatterns = [
   
    path ("inicio/", views.PagosRead.as_view(), name = "index"),
    path ("login/", views.CustomLoginView.as_view(), name = "login"),
    path ("register/", views.register, name="register"),
    path ("logout/", LogoutView.as_view(template_name="empleado/logout.html"), name="logout"),
    path("notificaciones/create", views.NotificacionesCreate.as_view(), name="notificaciones_create"),
    path("pagos/detail/<pk>", views.PagosDetail.as_view(), name="pagos_detail"),
    path("vacaciones/detail/<pk>", views.VacacionesDetail.as_view(), name="vacaciones_detail"),
 
]