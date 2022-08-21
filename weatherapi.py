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

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("An error occurred.")