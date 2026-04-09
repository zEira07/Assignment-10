import urllib.request
import json

def get_weather():
    city = input("Enter city name: ")
    url = f"https://wttr.in/{city}?format=j1"

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())

        print("Weather:", data["current_condition"][0]["weatherDesc"][0]["value"])
        print("Temperature:", data["current_condition"][0]["temp_C"], "°C")

get_weather()