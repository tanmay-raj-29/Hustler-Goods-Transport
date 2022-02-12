from rest_framework import serializers
from .models import City, Route, Dealer, Driver

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'




class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'




class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = '__all__'




class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'