from flask import Flask, render_template
import requests
import os

API = os.getenv("OPEN_API_KEY")

def weather_info(city):
	response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}')
	return response


app = Flask(__name__)


@app.route('/')
def root():
	return "<h1> This is a weather app created by Kannan. </h1> <h4> Usage: http://localhost:5000/weather/cityname </h4>"

@app.route('/weather/<city>')
def weather(city):
	response = weather_info(city=city)
	return render_template('index.html',response=response)

if __name__ == '__main__':
    app.run(debug=True)
