from django.urls import path
from empleador import views

app_name = "empleador"
urlpatterns = [
   
    path ("inicio/", views.inicio, name = "index"),
    
    

]