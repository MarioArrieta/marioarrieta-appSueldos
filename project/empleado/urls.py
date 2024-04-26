from django.urls import path
from empleado import views

app_name = "empleado"
urlpatterns = [
   
    path ("inicio/", views.inicio, name = "index"),
    
    

]