from django.contrib import admin
from django.urls import include, path
from guetbook import views  # Pastikan ini sudah benar
from guetbook.views import home

urlpatterns = [
    path('', views.home, name='home'),  # Menggunakan home dari guestbook/views.py
    path('guetbook/', include('guetbook.urls')),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]
