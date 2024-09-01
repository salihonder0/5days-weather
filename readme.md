# Weather Data Fetcher

This is a Flask-based web application that allows users to select a city and retrieve weather data, including temperature, humidity, weather description, and an associated icon.

## Features

- **City Selection**: Users can select a city to fetch real-time weather data.
- **Weather Information**: The application displays the following data for the selected city:
  - Date and Time
  - Temperature
  - Humidity
  - Weather Description
  - Weather Icon

## Project Structure

- `app.py`: Main application file that handles routing and API requests.
- `templates/`: Contains HTML templates used for rendering the web pages.
- `API`: Contains API datas to fetch weather info.

## Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/salihonder0/weather-data-fetcher.git
    cd weather-data-fetcher
    ```

2. Create a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api).

4. Set the API key in your environment:

    ```bash
    export WEATHER_API_KEY='your_api_key'  # On Windows: set WEATHER_API_KEY='your_api_key'
    ```

### Running the Application

1. Start the Flask server:

    ```bash
    flask run
    ```

2. Open your browser and go to `http://127.0.0.1:5000/`.

### Example Code

Here’s an example of how the weather data is extracted from the API response in the application:

```python
weather_data = {
    "date": day["dt_txt"],
    "temperature": day["main"]["temp"],
    "humidity": day["main"]["humidity"],
    "description": day["weather"][0]["description"],
    "icon": day["weather"][0]["icon"],
}
