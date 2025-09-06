# backend/ai_model.py

def predict_watering_schedule(sensor_data, weather_data):
    """
    A simulated AI model that provides a more nuanced decision.
    In a real-world scenario, this would use a trained ML model (e.g., scikit-learn).
    """
    moisture = sensor_data["soil_moisture"]
    is_raining = weather_data["is_raining"]

    # Basic rule-based logic remains
    if is_raining:
        return {"decision": "OFF", "reason": "AI predicts no water needed due to rain.", "duration": 0}
    
    if moisture > 60:
         return {"decision": "OFF", "reason": "AI predicts optimal moisture levels.", "duration": 0}

    # Here's the "smarter" part: the duration changes based on conditions
    if 40 <= moisture <= 60:
        duration = 5 # Just a little bit of water
        reason = "AI recommends a short cycle to maintain moisture."
    elif 25 <= moisture < 40:
        duration = 12 # A standard watering cycle
        reason = "AI recommends a standard cycle to correct dryness."
    else: # moisture < 25
        duration = 20 # A long watering cycle for very dry soil
        reason = "AI recommends a long cycle for very dry soil."

    return {"decision": "ON", "reason": reason, "duration": duration}