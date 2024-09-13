from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    error_message = None

    if request.method == 'POST':
        location = request.form.get('city')  # This could be either a city name or ZIP code

        if location:
            api_key = os.getenv('OPENWEATHER_API_KEY')
            
            # Determine if the input is a ZIP code (numeric) or a city name (contains letters)
            if location.isdigit():  # ZIP code (assume it's for the US, can expand to handle other countries)
                url = f'http://api.openweathermap.org/data/2.5/weather?zip={location},US&appid={api_key}&units=imperial'
            else:  # City name
                url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial'

            print(f"Requesting URL: {url}")

            response = requests.get(url)
            print(f"API Response: {response.text}")

            if response.status_code == 200:
                weather_data = response.json()
            else:
                error_message = f"Could not retrieve weather data for {location}. Please try again."

    return render_template('index.html', weather=weather_data, error=error_message)
