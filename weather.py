import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
CITY = os.getenv("CITY", "Taipei")

def get_weather_text():
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=zh_tw"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            return "天氣資訊讀取失敗 ❌"

        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"天氣：{weather} 🌡 {temp:.1f}°C"

    except Exception as e:
        return f"無法取得天氣資訊 🚫"