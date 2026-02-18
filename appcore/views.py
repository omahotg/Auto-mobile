from django.shortcuts import render
from products.models import Vehicle

def home(request):
    vehicles = Vehicle.objects.all()
    context = {'vehicles': vehicles}
    return render(request, 'home.html', context)

