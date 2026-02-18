from django.urls import path
from . import views


urlpatterns = [
    path('', views.cars, name = 'product-cars'),
    # path('', views.detail, name = 'detail-page'),
    path('<int:pk>/', views.detail, name='detail-page'),
    
    
]