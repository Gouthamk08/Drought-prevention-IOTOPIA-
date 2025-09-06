// The URL of the backend API
const API_URL = "http://127.0.0.1:5000/api/system-status";

// --- CHART SETUP ---
const moistureChartCanvas = document.getElementById('moistureChart');
const moistureChart = new Chart(moistureChartCanvas, {
    type: 'line',
    data: {
        labels: [], // Timestamps will go here
        datasets: [{
            label: 'Soil Moisture',
            data: [], // Moisture data will go here
            borderColor: '#4ecdc4',
            backgroundColor: 'rgba(78, 205, 196, 0.1)',
            fill: true,
            tension: 0.4
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true,
                max: 100
            }
        },
        animation: {
            duration: 400
        }
    }
});
// --- END CHART SETUP ---

// Main function to fetch data and update the UI
async function updateDashboard() {
    try {
        const response = await fetch(API_URL);
        const data = await response.json();

        // Update the sensor data cards
        document.getElementById("moisture-level").textContent = `${data.sensor_data.soil_moisture} %`;
        document.getElementById("temp-level").textContent = `${data.sensor_data.temperature} °C`;
        document.getElementById("weather-status").textContent = data.weather_data.is_raining ? "Raining 🌧️" : "Clear ☀️";
        document.getElementById("ai-duration").textContent = `${data.irrigation_status.duration} mins`;
        
        // Update the main status card
        const statusElement = document.getElementById("irrigation-status");
        const reasonElement = document.getElementById("reason");
        
        statusElement.textContent = `WATERING: ${data.irrigation_status.decision}`;
        reasonElement.textContent = data.irrigation_status.reason;

        // Change color based on status for a better visual cue
        if (data.irrigation_status.decision === "ON") {
            statusElement.style.color = "var(--accent-color-on)"; // Green
        } else {
            statusElement.style.color = "var(--accent-color-off)"; // Red
        }

        // --- CHART UPDATE LOGIC ---
        const now = new Date();
        const currentTime = `${now.getHours()}:${String(now.getMinutes()).padStart(2, '0')}:${String(now.getSeconds()).padStart(2, '0')}`;
        const moistureData = data.sensor_data.soil_moisture;

        moistureChart.data.labels.push(currentTime);
        moistureChart.data.datasets[0].data.push(moistureData);

        // Limit the chart to the last 15 data points
        if (moistureChart.data.labels.length > 15) {
            moistureChart.data.labels.shift();
            moistureChart.data.datasets[0].data.shift();
        }
        moistureChart.update();
        // --- END CHART UPDATE LOGIC ---

    } catch (error) {
        console.error("Failed to fetch data:", error);
        document.getElementById("reason").textContent = "Error connecting to the backend.";
    }
}

// Update the dashboard every 3 seconds
setInterval(updateDashboard, 3000);

// Run once as soon as the page loads
document.addEventListener('DOMContentLoaded', updateDashboard);