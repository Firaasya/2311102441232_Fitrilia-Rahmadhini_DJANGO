from django.shortcuts import render, redirect
from .models import Guest

def home(request):
    return render(request, 'home.html')

def guestbook_list(request):
    guests = Guest.objects.all().order_by('-date')
    return render(request, 'guestbook_list.html', {'guests': guests})

def guestbook_view(request):
    # logika view disini
    return render(request, 'guestbook_list.html')

def add_guest(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            Guest.objects.create(name=name, email=email, message=message)
            return redirect('guestbook_list')
        
    return render(request, 'add_guest.html')
