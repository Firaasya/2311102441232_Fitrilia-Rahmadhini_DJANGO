from django.urls import include, path
from .views import guetbook_list, add_guet
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('guetbook.urls')),
]

urlpatterns = [
    path('', guetbook_list, name='guetbook_list'),
    path('add/', add_guet, name='add_guet'),
]
