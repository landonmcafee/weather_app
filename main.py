# basic beginnings of a weather app

import requests
import config

# api key from openweathermap.org
api_key = config.api_key

user_input = input('Enter city: ')
# print(user_input) testing printing to console

# fetch url and store in variable
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

while weather_data.json()['cod'] == '404':
    print('No city found.')
    user_input = input('Enter city: ')
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

    # print(weather_data.status_code) testing status code

weather = weather_data.json()['weather'][0]['main']
temp = round(weather_data.json()['main']['temp'])

print(f"The weather in {user_input} is {weather}.")
print(f"The temperature in {user_input} is {temp}°F.")



