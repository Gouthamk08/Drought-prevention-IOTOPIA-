# backend/weather.py
import requests

# Paste your API key here
API_KEY = "YOUR_API_KEY"
BENGALURU_LAT = "12.9716"
BENGALURU_LON = "77.5946"
API_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={BENGALURU_LAT}&lon={BENGALURU_LON}&appid={API_KEY}"

def get_weather_forecast():
    """Checks if rain is detected in Bengaluru."""
    try:
        response = requests.get(API_URL).json()
        weather_condition = response['weather'][0]['main']
        if weather_condition.lower() == 'rain':
            return {"is_raining": True}
    except Exception as e:
        print(f"Could not fetch weather data: {e}")
        return {"is_raining": False}
    return {"is_raining": False}
