from flask import Flask, send_file
from weather import get_weather_text

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('UI.html')

@app.route('/weather')
def weather():
    return get_weather_text()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)