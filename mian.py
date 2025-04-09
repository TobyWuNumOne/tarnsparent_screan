# -*- coding: utf-8 -*-
# @Time    : 2023/10/8 17:00
# @Author  : TobyWu
# @File    : main.py
# @Software: PyCharm
# @Project : Raspberry Pi 智慧時鐘
import tkinter as tk
import time
from tkinter import ttk
from ttkbootstrap import Style

# 建立主視窗，使用 minty 主題
style = Style(theme="minty")
window = style.master
window.title("智慧時鐘")
window.attributes('-fullscreen', True)
window.bind("<Escape>", lambda e: window.destroy())

def get_weather_text():
    # 未來可以接 API，這裡先放假資料
    return "天氣：晴朗 ☀️  25°C"

def update_clock():
    # 更新時間
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

def update_weather():
    # 更新天氣
    weather_info = get_weather_text()
    weather_label.config(text=weather_info)
    weather_label.after(60000, update_weather)  # 每分鐘更新一次

# 顯示時間的標籤
clock_label = tk.Label(window, font=("Helvetica", 80), bg="black", fg="white")
clock_label.pack(padx=20, pady=100)

# 顯示天氣的標籤
weather_label = tk.Label(window, font=("Helvetica", 28), bg="black", fg="lightgray")
weather_label.pack(side="bottom", pady=40)

update_clock()
update_weather()

window.mainloop()
