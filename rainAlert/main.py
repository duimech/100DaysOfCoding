# This program pulls weather data with an API and prints to bring an umbrella if its going to rain the next 12 hours. 
# Author: Ray Bolin
# Date: 2/17/2022
# 100DaysOfCoding

import requests
import os

endpoint = "https://api.openweathermap.org/data/2.5/onecall"

# Set environment variables before using this line
api_key = os.environ.get("API_KEY")
# api_key = "longapikeyhere"
api_parameters = {
    "lat": 29.760427,
    "lon": -95.369804,
    "units": "imperial",
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

api_response = requests.get(endpoint, params=api_parameters)
api_response.raise_for_status()
weather_data = api_response.json()
twelve_hour_data = weather_data["hourly"][:12]

will_rain = False
for hour in twelve_hour_data:
    condition_code = int(hour["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")

# i = 0
# while i < 12:
#     if weather_data["hourly"][i]["weather"][0]["id"] < 700:
#         will_rain = True
#     i += 1
# if will_rain:
#     print("Bring an umbrella.")



