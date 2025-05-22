import requests
import csv
import os

API_KEY = "dcfde662f6aee320f506e7a32a71d73e"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        weather = {
            "City": city,
            "Temperature (°C)": data["main"]["temp"],
            "Humidity (%)": data["main"]["humidity"],
            "Condition": data["weather"][0]["main"]
        }
        return weather
    else:
        print("Error:", data.get("message", "Unknown error"))
        return None

def save_to_csv(weather, filename="Day 14/weather_data.csv"):
    file_exists = os.path.isfile(filename)

    with open(filename, mode='a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=weather.keys())
        if not file_exists or os.stat(filename).st_size == 0:
            writer.writeheader()
        writer.writerow(weather)

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather = fetch_weather(city)
    if weather:
        save_to_csv(weather)
        print("Weather data saved.")
