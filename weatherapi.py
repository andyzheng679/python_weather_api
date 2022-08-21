from urllib import response
import requests

# GET = retrieve information
# HEAD = retrieve resource headers
# POST = submit data to the server
# PUT = save an object at the location
# DELETE = delete the object at the location

API_KEY = "41cbf48bcfd9a75a3beaab228c2a9e13"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(requests_url)

#{'coord': {'lon': -74.006, 'lat': 40.7143}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}], 
#'base': 'stations', 'main': {'temp': 295.86, 'feels_like': 296.17, 'temp_min': 291.95, 'temp_max': 297.56, 'pressure': 1020, 'humidity': 76}, 'visibility': 10000, 'wind': {'speed': 3.13, 'deg': 168, 'gust': 4.02}, 'clouds': {'all': 30}, 'dt': 1661061429, 'sys': {'type': 2, 'id': 2039034, 'country': 'US', 'sunrise': 1661076743, 'sunset': 1661125578}, 'timezone': -14400, 'id': 5128581, 'name': 'New York', 'cod': 
#200}

#[{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]
#295.84

# temperature is in Kelvin, -273.15 to convert to celsius, * 1.8 then + 32 to convert to Fahrenheit

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print("Weather:", weather)
    temperature = ((round(data["main"]["temp"] -273.15, 2) * 1.8) + 32)
    print("Temperature:", temperature)
else:
    print("An error occurred.")