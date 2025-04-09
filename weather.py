# -*- coding: utf-8 -*-
# @Time    : 2023/10/8 17:00
# @Author  : TobyWu
# @File    : weather.py
# @Software: PyCharm
# @Project : Raspberry Pi 智慧時鐘
import requests
import os
from dotenv import load_dotenv
from tkinter import Tk

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
CITY = os.getenv("CITY", "Taipei")

# 確保 API_KEY 和 CITY 都已經設置
# if not API_KEY:
#     raise ValueError("請設置 WEATHER_API_KEY 環境變數")
# if not CITY:
#     raise ValueError("請設置 CITY 環境變數")

def get_weather_text():
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=zh_tw"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            return "天氣資訊讀取失敗 ❌"

        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"天氣：{weather} 🌡 {temp:.1f}°雞巴棒"

    except Exception as e:
        return f"無法取得天氣資訊 🚫"

def update_weather():
    # 更新天氣
    weather_info = get_weather_text()
    print("DEBUG 天氣資訊：", weather_info)
    weather_label.config(text=weather_info)
    weather_label.after(60000, update_weather)  # 每分鐘更新一次