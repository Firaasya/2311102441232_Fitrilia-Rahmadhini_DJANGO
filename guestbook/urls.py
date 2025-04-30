from django.urls import include, path
from .views import guestbook_list, add_guest, guestbook_view
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', guestbook_list, name='guestbook_list'),
    path('guestbook/', guestbook_view, name='guestbook'), 
    path('add-guests/', add_guest, name='add_guest'),
]
