# I have used generic/online openweathermap api key. you can get your own api key from openweathermap.

import requests
import sys

def get_weather(location):
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = 'bd5e378503939ddaee76f12ad7a97608'
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    forecast_url = 'https://api.openweathermap.org/data/2.5/forecast'

    # Retrieve current weather information
    params = {'q': location, 'appid': api_key, 'units': 'metric'}
    response = requests.get(base_url, params=params)
    data = response.json()

    if data['cod'] == 200:
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"Current weather in {location}: {weather}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

        # Retrieve 5-day weather forecast
        forecast_params = {'q': location, 'appid': api_key, 'units': 'metric', 'cnt': 5}
        forecast_response = requests.get(forecast_url, params=forecast_params)
        forecast_data = forecast_response.json()

        if forecast_data['cod'] == "200":
            print("\n5-Day Weather Forecast:")
            for entry in forecast_data['list']:
                date = entry['dt_txt']
                description = entry['weather'][0]['description']
                temp = entry['main']['temp']
                print(f"{date}: {description}, {temp}°C")
        else:
            print("Unable to retrieve the 5-day forecast.")

    else:
        print("Location not found or weather data unavailable.")

if len(sys.argv) != 2:
    print("Usage: python weather.py <location>")
else:
    location = sys.argv[1]
    get_weather(location)
