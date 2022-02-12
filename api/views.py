from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import City, Route, Dealer, Driver
from .serializers import CitySerializer, RouteSerializer, DealerSerializer, DriverSerializer

# Create your views here.
@api_view(['GET'])
def cities(request):
    cities = City.objects.all()
    serializer = CitySerializer(cities, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def routes(request):
    routes = Route.objects.all()
    serializer = RouteSerializer(routes, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def dealers(request):
    dealers = Dealer.objects.all()
    serializer = DealerSerializer(dealers, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def drivers(request):
    drivers = Driver.objects.all()
    serializer = DriverSerializer(drivers, many=True)
    return Response(serializer.data)