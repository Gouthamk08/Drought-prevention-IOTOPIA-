# backend/logic.py
MOISTURE_THRESHOLD = 35.0

def decide_watering(sensor_data, weather_data):
    """Decides if the system should water based on rules."""
    moisture = sensor_data["soil_moisture"]
    is_raining = weather_data["is_raining"]
    if moisture < MOISTURE_THRESHOLD and not is_raining:
        return {"decision": "ON", "reason": "Soil is dry and no rain is detected."}
    elif moisture >= MOISTURE_THRESHOLD:
        return {"decision": "OFF", "reason": "Soil has sufficient moisture."}
    else:
        return {"decision": "OFF", "reason": "It is currently raining."}
