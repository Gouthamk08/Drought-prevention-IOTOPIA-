# 💧 AI-Powered Smart Irrigation System with Blockchain Ledger

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)]()
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)]()
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)]()
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)]()

A full-stack web application developed for the IOTOPIA 2025 hackathon. This project addresses water scarcity in drought-prone agricultural zones by using a data-driven approach to optimize irrigation, enhanced with a transparent blockchain ledger for water usage auditing.


*(Live dashboard showing real-time sensor data, AI recommendations, and system status.)*

---
## ✨ Features

* **Live Dashboard:** A clean, responsive user interface to monitor real-time (simulated) soil moisture and temperature data.
* **Predictive AI:** A smart decision engine that goes beyond simple rules, recommending variable watering durations based on soil conditions and weather.
* **Real-time Weather Integration:** Utilizes the OpenWeather API to fetch live weather data, automatically halting irrigation during rain.
* **Blockchain Ledger:** Every watering cycle is recorded as an immutable transaction on a simulated blockchain, ensuring a transparent and auditable log of water consumption.
* **Data Visualization:** A live-updating chart that visualizes soil moisture trends over time.

---
## 🛠️ Technology Stack

This project is a full-stack application built with the following technologies:

* **Backend:**
    * **Python:** Core programming language.
    * **Flask:** A lightweight web framework used to build the backend server and API.
    * **OpenWeather API:** For fetching real-time weather data.
* **Frontend:**
    * **HTML5, CSS3, Vanilla JavaScript:** For the structure, styling, and interactivity of the dashboard.
    * **Chart.js:** For rendering the live data visualization chart.
* **Key Concepts Implemented:**
    * **IoT Simulation:** A Python script simulates real-time data from farm sensors.
    * **AI/ML (Simulated):** The `ai_model.py` mimics a predictive model to provide intelligent watering schedules.
    * **Blockchain (Simulated):** `blockchain.py` implements a simple, functional blockchain to log transactions.

---
## 🚀 How to Run Locally

To get this project running on your local machine, follow these steps.

**Prerequisites:**
* Python 3.x
* An API key from [OpenWeatherMap](https://openweathermap.org/api)

**1. Clone the repository:**
```bash
git clone https://github.com/Gouthamk08/smart-irrigation-hackathon.git
cd smart-irrigation-hackathon/backend

Of course. Here is the entire "How to Run Locally" section, with all steps included, in a single block for easy copying.

````markdown
## 🚀 How to Run Locally

To get this project running on your local machine, follow these steps.

**Prerequisites:**
* Python 3.x
* Git
* A free API key from [OpenWeatherMap](https'://openweathermap.org/api')

---
**Step 1: Clone the Repository**
Open your terminal and run this command to download the project files:
```bash
git clone [https://github.com/Gouthamk08/Drought-prevention-IOTOPIA-.git](https://github.com/Gouthamk08/Drought-prevention-IOTOPIA-.git)
````

-----

**Step 2: Navigate to the Project Directory**

```bash
cd Drought-prevention-IOTOPIA-/backend
```

-----

**Step 3: Set Up the Virtual Environment**
This creates an isolated environment for the Python libraries.

```bash
# Create the virtual environment
python -m venv venv

# Activate it
# On Windows:
# venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

-----

**Step 4: Install Dependencies**
This command installs all the required libraries from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

-----

**Step 5: Add Your API Key**

1.  Open the `backend/weather.py` file in a text editor.
2.  Replace the placeholder `"YOUR_API_KEY_HERE"` with your actual OpenWeatherMap API key.
3.  Save and close the file.

-----

**Step 6: Run the Server**
Now, start the Flask application.

```bash
python app.py
```

-----

**Step 7: View the Application**
Your project is now running\!

  * Open your web browser and navigate to: **`http://127.0.0.1:5000`**

The smart irrigation dashboard should now be fully functional.

```
```
