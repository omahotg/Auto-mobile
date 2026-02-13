from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'product_home'),
    path('cars/', views.cars, name = 'product_cars'),
]