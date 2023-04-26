import requests
from flask import Flask, request, render_template
import os

app = Flask(__name__)

WEATHER_API = "http://api.weatherstack.com/current"
API_KEY = os.environ["WEATHER_API_KEY"]

# response = requests.get(f"{WEATHER_API}?access_key={API_KEY}&query='London'")
# response.raise_for_status()
# data = response.json()
# # print(data)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form.get('city')
        country = request.form.get('country')
        api_key = API_KEY

        weather_url = requests.get(f"{WEATHER_API}?access_key={api_key}&query={city}, {country}&units=m")
        weather_data = weather_url.json()

        weather = weather_data['current']['weather_descriptions'][0]
        temp = weather_data['current']['temperature']
        humidity = weather_data['current']['humidity']

        return render_template('result.html', weather=weather, temp=temp, humidity=humidity, city=city)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
