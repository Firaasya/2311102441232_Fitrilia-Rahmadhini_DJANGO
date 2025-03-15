from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'about.html')  

def home(request):
    return HttpResponse("Welcome to the Homepage!")