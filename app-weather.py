import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = "3e4693464dc0861f0d481c25c396a2bf"

def get_weather_data(location):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

def format_weather_data(data):
    current_weather = data["list"][0]
    forecast_weather = data["list"][1:]

    current_weather_summary = {
        "temperature": current_weather["main"]["temp"] / 10 ,
        "humidity": current_weather["main"]["humidity"],
        "description": current_weather["weather"][0]["description"],
        "icon": current_weather["weather"][0]["icon"],
    }

    forecast_weather_summary = []
    for day in forecast_weather:
        forecast_weather_summary.append({
            "date": day["dt_txt"],
            "temperature": round(current_weather["main"]["temp"] / 10 , 2),
            "humidity": day["main"]["humidity"],
            "description": day["weather"][0]["description"],
            "icon": day["weather"][0]["icon"],
        })

    return current_weather_summary, forecast_weather_summary

@app.route("/", methods=["GET", "POST"])
def weather_forecast():
    location = "Ankara"  # Default location

    if request.method == "POST":
        location = request.form["location"]

    weather_data = get_weather_data(location)
    current_weather_summary, forecast_weather_summary = format_weather_data(weather_data)

    return render_template("index.html", location=location, current_weather=current_weather_summary, forecast_weather=forecast_weather_summary)

if __name__ == "__main__":
    app.run(debug=True)
