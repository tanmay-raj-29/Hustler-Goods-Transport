from django.urls import path
from . import views

urlpatterns = [
    path('cities/', views.cities, name='cities'),
    path('routes/', views.routes, name='routes'),
    path('dealers/', views.dealers, name='dealers'),
    path('drivers/', views.drivers, name='drivers'),
]