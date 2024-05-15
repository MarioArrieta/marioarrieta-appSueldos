from django.urls import path
from core import views
from django.contrib.auth.views import LogoutView

app_name = "core"
urlpatterns = [
   
    path ("", views.inicio, name = "index"),
    path ("logout/", LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    
    

]