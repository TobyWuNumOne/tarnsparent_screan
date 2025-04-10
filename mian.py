# -*- coding: utf-8 -*-
# @Time    : 2023/10/8 17:00
# @Author  : TobyWu
# @File    : main.py
# @Software: PyCharm
# @Project : Raspberry Pi 智慧時鐘
import tkinter as tk
import time
import weather
import sys
from tkinter import ttk
from ttkbootstrap import Style


style = Style(theme="minty")
window = style.master
window.title("智慧時鐘")
window.attributes('-fullscreen', True)
window.bind("<Escape>", lambda e: window.destroy())
# window.configure(bg="#FFFFFF")

def update_clock():
    # 更新時間
    current_time = time.strftime("%H:%M:%S")
    hour, minute, second = current_time.split(':')
    hour_label.config(text=hour)
    minute_label.config(text=minute)
    second_label.config(text=second)
    # 每秒更新一次
    hour_label.after(1000, update_clock)

def update_weather():
    # 更新天氣
    weather_info = weather.get_weather_text()
    weather_label.config(text=weather_info)
    weather_label.after(60000, update_weather)  # 每分鐘更新一次

# 顯示小時的標籤
hour_label = tk.Label(window, font=("Courier New", 100, "bold"), bg="#FFFFFF", fg="#000000")
hour_label.place(x=40, y=30)

# 顯示分鐘的標籤
minute_label = tk.Label(window, font=("Courier New", 80, "bold"), bg="#FFFFFF", fg="#000000")
minute_label.place(x=180, y=45)

# 顯示秒鐘的標籤
second_label = tk.Label(window, font=("Courier New", 60, "bold"), bg="#FFFFFF", fg="#000000")
second_label.place(x=300, y=60)

# 顯示天氣的標籤
weather_label = tk.Label(window, font=("Helvetica", 28, "bold"), bg="#FFFFFF", fg="#000000")
weather_label.place(relx=0.25, rely=0.95, anchor="se")

update_clock()
update_weather()

window.mainloop()