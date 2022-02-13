from django.urls import path
from . import views

urlpatterns = [
    path('cities/', views.cities, name='cities'),
    path('cities/<int:pk>/dealers', views.city_dealers, name='city_dealers'),

    path('routes/', views.routes, name='routes'),
    path('routes/<int:pk>/drivers/', views.route_drivers, name='route_drivers'),
    
    path('dealers/', views.dealers, name='dealers'),
    path('dealers/<int:pk>/', views.dealer, name='dealer'),
    
    path('drivers/', views.drivers, name='drivers'),
    path('drivers/<int:pk>/', views.driver, name='driver'),
]