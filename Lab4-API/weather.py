import os
import requests
from pprint import pprint
from datetime import datetime
try:
    # Minneapolis
    lat = 44.97
    lon = -93.26
    units = 'metric'  # change to 'imperial' for quantities in Fahrenheit, miles per hour etc.

    api_key = "fcfd3c850029434b567d71fcf30afd8e"
    #api_key = os.environ['WEATHER_KEY']  # Set this environment variable on your computer

    # use a dic for query parameter
    url = f'https://api.openweathermap.org/data/2.5/forecast'
    query = {'lat': lat,
            'lon': lon,
            'units': units,
            'appid': api_key
            }

    response = requests.get(url, params=query)
    #response.raise_for_status()
    weather_forecast = response.json()
    print(weather_forecast)
    #pprint(weather_forecast)

    forecast = weather_forecast['list']

    for time_period in forecast:
        print(time_period)
        dt = time_period['dt']
        human_date = datetime.fromtimestamp(dt)
        print(human_date)
        weather = time_period['weather']
        #print(weather_description)
        for weather_item in weather:
            print(weather_item['description'])

        #tempetures
        temp = '14C'
        print(f'{str(human_date):<30} {temp:<30}')

except Exception as e:
    print(e)