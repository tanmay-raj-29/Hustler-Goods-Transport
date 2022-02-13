from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import City, Route, Dealer, Driver
from .serializers import CitySerializer, RouteSerializer, DealerSerializer, DriverSerializer
from django.http import HttpResponse

# Create your views here.
@api_view(['GET'])
def cities(request):
    cities = City.objects.all()
    serializer = CitySerializer(cities, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def city_dealers(request, pk):
    city = City.objects.get(pk=pk)
    dealers = city.dealer_set.all()
    serializer = DealerSerializer(dealers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def routes(request):
    routes = Route.objects.all()
    serializer = RouteSerializer(routes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def route_drivers(request, pk):
    route = Route.objects.get(pk=pk)
    drivers = route.driver_set.all()
    serializer = DriverSerializer(drivers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def dealers(request):
    dealers = Dealer.objects.all()
    serializer = DealerSerializer(dealers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def dealer(request, pk):
    try:
        dealer = Dealer.objects.get(pk=pk)
    except Dealer.DoesNotExist:
        return HttpResponse(status=404)
    serializer = DealerSerializer(dealer)
    return Response(serializer.data)


@api_view(['GET'])
def drivers(request):
    drivers = Driver.objects.all()
    serializer = DriverSerializer(drivers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def driver(request, pk):
    try:
        driver = Driver.objects.get(pk=pk)
    except Driver.DoesNotExist:
        return HttpResponse(status=404)
    serializer = DriverSerializer(driver)
    return Response(serializer.data)