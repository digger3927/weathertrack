# WeatherTrack

WeatherTrack is a simple Flask application that allows users to retrieve weather information for a city or ZIP code using the OpenWeatherMap API. The app is containerized using Docker and deployed to Google Cloud Run.
Features
Retrieve current weather for a given city or ZIP code.
Displays temperature, weather description, and humidity.
Built with Flask, styled with CSS, and uses the OpenWeatherMap API.
Deployed using Docker and Google Cloud Run.

## Table of Contents
Prerequisites
Local Setup
Clone the Repository
Install Dependencies
Running Locally
Using Docker
Build and Run the Container
Development Mode with Docker Volumes
Deployment to Google Cloud Run
Environment Variables
API Reference

## Prerequisites
Make sure you have the following installed on your machine:
Python 3.9 or above
Docker
Google Cloud SDK (if deploying to Google Cloud Run)
You also need an OpenWeatherMap API key. You can get it by signing up for free at OpenWeatherMap.

## Local Setup
Clone the Repository
First, clone this repository to your local machine:
bash
Copy code
git clone https://github.com/YOUR_USERNAME/weathertrack.git
cd weathertrack

## Install Dependencies
Create a virtual environment and install the required dependencies:
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

## Running Locally
Before running the app, create a .env file in the root directory and add your OpenWeatherMap API key:
bash
Copy code
OPENWEATHER_API_KEY=your_openweathermap_api_key

Now you can run the app locally:
bash
Copy code
python run.py

Visit http://127.0.0.1:8080 in your browser to see the app running.

## Using Docker
Build and Run the Container
You can build and run the app inside a Docker container. First, build the Docker image:
bash
Copy code
docker build -t weathertrack .

Then, run the container:
bash
Copy code
docker run -p 8080:8080 weathertrack

Visit http://localhost:8080 in your browser to view the app.
Development Mode with Docker Volumes
For development, you can use Docker volumes to automatically sync your local files with the container. This way, you don't need to rebuild the image every time you make a change:
bash
Copy code
docker run -it --rm -v "$(pwd):/app" -p 8080:8080 weathertrack

Now, any changes you make to your local files will be immediately reflected in the container.

## Deployment to Google Cloud Run
To deploy the app to Google Cloud Run, follow these steps:
### Prerequisites
Install and configure the Google Cloud SDK: Google Cloud SDK.
Enable the Cloud Run API and Container Registry API in your Google Cloud project.
Steps
Authenticate with your Google Cloud account:
bash
Copy code
gcloud auth login


Build and Push Docker Image to Google Container Registry (GCR):
bash
Copy code
docker build -t gcr.io/YOUR_PROJECT_ID/weathertrack .
docker push gcr.io/YOUR_PROJECT_ID/weathertrack


## Deploy to Cloud Run:
bash
Copy code
gcloud run deploy weathertrack \
    --image gcr.io/YOUR_PROJECT_ID/weathertrack \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated


Once deployed, you will get a public URL for the app.

## Environment Variables
This app requires the following environment variables:
Key
Description
OPENWEATHER_API_KEY
Your API key from OpenWeatherMap

For local development, create a .env file in the root of your project, and add your OpenWeatherMap API key there:
env
Copy code
OPENWEATHER_API_KEY=your_openweathermap_api_key


### API Reference
This app uses the OpenWeatherMap API to retrieve current weather data.
Endpoint: http://api.openweathermap.org/data/2.5/weather
Method: GET
Parameters:
q: City name or ZIP code
appid: Your OpenWeatherMap API key
units: Units of measurement (imperial for Fahrenheit, metric for Celsius)

### Contributing
Feel free to submit pull requests to improve the project. All contributions are welcome!

#### License
This project is licensed under the MIT License - see the LICENSE file for details.

