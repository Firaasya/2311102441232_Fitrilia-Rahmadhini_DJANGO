from django.shortcuts import render, redirect
from .models import Guet

def home(request):
    return render(request, 'guetbook/home.html')

def guetbook_list(request):
    guets = Guet.objects.all().order_by('-date')
    return render(request, 'guetbook/guetbook_list.html', {'guets': guets})

def add_guet(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            Guet.objects.create(name=name, email=email, message=message)
            return redirect('guetbook_list')
        
    return render(request, 'guetbook/add_guet.html')
