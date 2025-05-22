# weather_utils.py
class WeatherData:
    def __init__(self, city, temperature, humidity, condition):
        self.city = city
        self.temperature = temperature
        self.humidity = humidity
        self.condition = condition

    def to_dict(self):
        return {
            "City": self.city,
            "Temperature (°C)": self.temperature,
            "Humidity (%)": self.humidity,
            "Condition": self.condition
        }
