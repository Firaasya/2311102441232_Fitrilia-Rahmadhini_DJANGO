from django.contrib import admin
from django.urls import include, path
from guestbook import views  
from guestbook.views import home

urlpatterns = [
    path('', views.home, name='home'),  
    path('guestbook/', include('guestbook.urls')),
    path('admin/', admin.site.urls),
]