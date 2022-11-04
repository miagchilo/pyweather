from flask import Flask, render_template,request
import requests


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method =='POST':
        city_name = request.form.get('city')

        r = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid=d02fc7cca661cb50364a593d1e089c09')

        json_object = r.json()

        temperature = int(json_object['main']['temp']-273.15)
        humidity = int(json_object['main']['humidity'])
        pressure = int(json_object['main']['pressure'])
        wind = int(json_object['wind']['speed'])

        condition = json_object['weather'][0]['main']
        desc = json_object['weather'][0]['description']

        return render_template('home.html',temperature=temperature,pressure=pressure,humidity=humidity,city_name=city_name,condition=condition,wind=wind,desc=desc)
    else:
        return render_template('home.html') 

if __name__ == '__main__':
    app.run(debug=True)

# api_key = 'd02fc7cca661cb50364a593d1e089c09'

# user_input = input("Enter city:")


# weather_data = requests.get(
#     f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

# # print(weather_data.json())

# weather = weather_data.json()['weather'][0]['main']
# temp = round(weather_data.json()['main']['temp'])

# print(f"The weather in {user_input} is: {weather}")
# print(f"The temperature in {user_input} is: {temp}")