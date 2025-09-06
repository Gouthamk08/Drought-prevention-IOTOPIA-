from flask import Flask, jsonify
from flask_cors import CORS

# --- IMPORTS FOR NEW MODULES ---
from blockchain import blockchain
from ai_model import predict_watering_schedule
# --- ORIGINAL MODULES ---
from simulator import get_sensor_data
from weather import get_weather_forecast

# Initialize the Flask app
app = Flask(__name__)
# Enable CORS to allow your frontend to make requests to this backend
CORS(app)


# --- MAIN API ENDPOINT ---
@app.route("/api/system-status")
def system_status():
    """This is the main API endpoint that the frontend will call."""
    
    # 1. Get data from sensors and weather API
    sensors = get_sensor_data()
    weather = get_weather_forecast()
    
    # 2. Use the new, smarter AI model to make a decision
    decision = predict_watering_schedule(sensors, weather)

    # 3. --- BLOCKCHAIN INTEGRATION ---
    # If the AI decides to water, log it as a transaction on the blockchain
    if decision['decision'] == "ON":
        # Create the transaction with the duration recommended by the AI
        blockchain.new_transaction(
            sensor_data=sensors,
            water_duration=decision['duration']
        )
        
        # In a hackathon, we can "mine" a new block immediately after a transaction
        last_block = blockchain.last_block
        proof = 12345  # A dummy proof-of-work for demonstration
        previous_hash = blockchain.hash(last_block)
        blockchain.new_block(proof, previous_hash)
    # --- END OF BLOCKCHAIN INTEGRATION ---

    # 4. Combine all information into a single response for the frontend
    response = {
        "sensor_data": sensors,
        "weather_data": weather,
        "irrigation_status": decision
    }
    
    # 5. Return the response as JSON
    return jsonify(response)


# --- NEW ENDPOINT TO VIEW THE LEDGER ---
@app.route('/api/water-ledger', methods=['GET'])
def full_chain():
    """This endpoint returns the entire water usage ledger."""
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response)


# This part runs the server when you execute `python app.py`
if __name__ == "__main__":
    app.run(debug=True, port=5000)