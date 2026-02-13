from django.shortcuts import render
from .models import Vehicle

# Create your views here.

def home(request):
    vehicles = Vehicle.objects.all()
    context = {'vehicles': vehicles}
    return render(request, 'home.html', context)

def cars(request):
    return render(request, 'cars.html')