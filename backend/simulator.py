# backend/simulator.py
import random

def get_sensor_data():
    """Returns simulated soil moisture and temperature data."""
    soil_moisture = random.uniform(20.0, 85.0)
    temperature = random.uniform(24.0, 34.0)
    return {
        "soil_moisture": round(soil_moisture, 2),
        "temperature": round(temperature, 2)
    }
