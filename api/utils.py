import json
from .models import City

def get_cities():
    print("Getting Cities")

    City.objects.all().delete()
    
    f = open('cities.json')
    data = json.loads(f.read())

    for state in data['states']:
        state_name = state['name']
        print(state_name)
        for city in state['cities']:
            city_name = city['name']
            latitude = float(city['latitude'])
            longitude = float(city['longitude'])
            
            city_obj = City(
                name = city_name,
                state = state_name,
                latitude = latitude,
                longitude = longitude,
            )
            city_obj.save()


    f.close()
    print("Got cities")