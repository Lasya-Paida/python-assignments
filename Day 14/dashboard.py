# dashboard.py
import pandas as pd

def analyze_weather(filename="Day 14/weather_data.csv"):
    df = pd.read_csv(filename)

    print("\n📊 Weather Summary:")
    print(df.describe())

    print("\n🌆 Average temperature by city:")
    print(df.groupby("City")["Temperature (°C)"].mean().round(2))

    print("\n🔝 Most common weather condition:")
    print(df["Condition"].value_counts())

if __name__ == "__main__":
    analyze_weather()
