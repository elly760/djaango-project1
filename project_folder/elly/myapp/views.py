from django.shortcuts import render
from .models import Student

def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
def register(request): 
    return render(request, 'register.html')