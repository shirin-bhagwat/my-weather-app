import requests
from flask import Flask
app = Flask(__name__)

@app.route('/weather/<string:zipcode>')
def get_weather(zipcode):
    url = "http://api.openweathermap.org/data/2.5/weather"
    apikey = "c25195fa7c62eb774a0603e1881fa8f5"
    cod = "us"
    report =  requests.get(url+"?zip="+zipcode +","+cod +"&APPID=" + apikey).content
    return report

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

