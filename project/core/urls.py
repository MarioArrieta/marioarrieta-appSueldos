from django.urls import path
from core import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static





app_name = "core"
urlpatterns = [
   
    path ("", views.inicio, name = "index"),
    path ("logout/", LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    
    

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

