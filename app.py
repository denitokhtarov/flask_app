from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import requests

app = Flask(__name__)
app.secret_key = 'frte4htiehgi'

@app.route('/', methods=['POST','GET'])
def home():
  if request.method == 'POST':
    try:
      city_name = request.form.get('city')
      r = requests.get(f'https://api.weatherapi.com/v1/current.json?key=73bd4bbc0ae843829bd75648231101&q={city_name}&aqi=no')
      json_object = r.json()

      temp = json_object['current']['temp_c']
      wind = json_object['current']['wind_kph']
      humidity = json_object['current']['humidity']
      vision = json_object['current']['vis_km']
      time = json_object['location']['localtime'][11:]
      return render_template('home.html',temp=temp,wind=wind, humidity=humidity, vision=vision, time=time)
    except:
      return render_template('home.html')
  else:
    return render_template('home.html')


if __name__ == '__main__':
  app.run(debug=True)