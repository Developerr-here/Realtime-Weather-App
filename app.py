from flask import Flask, redirect, render_template,url_for,request,jsonify
import os
import requests

# Json: javascript object notation



app = Flask(__name__)
API_KEY="65085301675a078c654d5de7d47c3176"

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/get_weather',methods=['POST'])
def get_weather():
    data=request.get_json()
    lat=data.get('lat')
    lon = data.get('lon')

    print(f"{lat} and {lon}")
    if not lat or not lon:
        return jsonify({'error':'Missing Coordinates'})
    
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

    try:
        res = requests.get(url).json()
        weather = {
            'location':f"{res['name']},{res['sys']['country']}",
            'temperature':res['main']['temp'],
            'description':res['weather'][0]['description'].capitalize(),
            # 'icon': f"https://api.openweathermap.org/img/wn/{res['weather'][0]['icon']}@zx.png"
            'icon': f"https://openweathermap.org/img/wn/{res['weather'][0]['icon']}@2x.png"


        }
        return jsonify(weather)
    except Exception as e:
        return jsonify({'error':'Failed to retrieve weather data'}),500


if __name__ == "__main__":
    app.run()


