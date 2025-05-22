import requests
import csv
import os
from datetime import datetime

API_KEY = "dcfde662f6aee320f506e7a32a71d73e"  # Your API key here
CSV_FILE = "weather_data.csv"

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print(f"Error: {data.get('message', 'Failed to get data')}")
            return None

        return {
            "city": data["name"],
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"]
        }
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def save_to_csv(weather_data):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode="a", newline="") as csvfile:
        fieldnames = ["city", "date", "temperature", "humidity", "weather"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(weather_data)
    print(f"Weather data saved to {CSV_FILE}")

def main():
    city = input("Enter city name: ").strip()
    weather_data = fetch_weather(city)
    if weather_data:
        print(f"Weather in {weather_data['city']} at {weather_data['date']}:")
        print(f"Temperature: {weather_data['temperature']} °C")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Condition: {weather_data['weather']}")
        save_to_csv(weather_data)

if __name__ == "__main__":
    main()
