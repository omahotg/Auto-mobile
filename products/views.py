from django.shortcuts import render
from .models import Vehicle, Category

# Create your views here.


def cars(request):
    brands = Category.objects.all()
    cars = Vehicle.objects.all()
    context = {'brands': brands, 'cars': cars}
    return render(request, 'cars.html', context)

def detail(request, pk):
    details = Vehicle.objects.get(id=pk)
    context = {'details': details}
    return render(request, 'product_details.html', context)