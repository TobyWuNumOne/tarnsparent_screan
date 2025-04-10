# -*- coding: utf-8 -*-
# @Time    : 2023/10/8 17:00
# @Author  : TobyWu
# @File    : weather.py
# @Software: PyCharm
# @Project : Raspberry Pi 智慧時鐘
import requests
import os
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')
API_KEY = os.getenv('KEY')
CITY = os.getenv('LOCATION')
# 讀取環境變數

if not API_KEY:
    raise ValueError("請設置 WEATHER_API_KEY 環境變數")
if not CITY:
    raise ValueError("請設置 CITY 環境變數")
# 確保環境變數已經設置

def get_weather_text():
    # 獲取天氣資訊
    weather_data = get_weather_data(CITY)
    simplified_data = simplify_data(weather_data)
    current_weather = get_current_weather(simplified_data)

    if current_weather is not None:
        text = f'位置: {CITY}<br>天氣概況: {current_weather["Wx"]}<br>降雨機率: {current_weather["PoP"]}<br>體感: {current_weather["CI"]}'
        return text
    else:
        return "無法獲取天氣資訊"



def get_weather_data(location):
    url = f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={API_KEY}&locationName=%E6%96%B0%E5%8C%97%E5%B8%82"
    params = {
        "locationName": location
        }
    
    headers = {
        "accept": "application/json"
    }
    # 設置請求的參數和標頭
    # 發送GET請求到API
    response = requests.get(url, params=params, headers=headers, timeout=10)


    if response.status_code == 200:
        try:
            # 將回應的JSON內容轉換為Python字典
            data = response.json()
            return data
        except ValueError:
            raise ValueError("API response is not valid JSON")
    else:
        raise ValueError(f"API request failed with status code {response.status_code}: {response.text}")
# 確保API請求成功，並且返回的數據是有效的JSON格式

def simplify_data(data):
    try:
        location_data = data['records']['location'][1] 
    except IndexError:
        location_data = data['records']['location'][0]
    # 確保獲取到正確的地點數據因為回傳好像都會包含新北市除了新北市只有新北市
    
    weather_elements = location_data['weatherElement']
    # 獲取天氣元素
    
    # 簡化數據結構
    simplified_data = {
        'location': location_data['locationName'],
    }

    for element in weather_elements:
        element_name = element['elementName']
        for time in element['time']:
            # 使用完整的開始時間作為鍵
            start_time = time['startTime']
            if start_time not in simplified_data:
                simplified_data[start_time] = {}

            parameter = time['parameter']
            parameter_str = parameter['parameterName']
            if 'parameterUnit' in parameter:
                parameter_str += f" {parameter['parameterUnit']}"

            # 尋找或創建對應時間的字典
            end_time = time['endTime']
            if end_time not in simplified_data[start_time]:
                simplified_data[start_time][end_time] = {}

            simplified_data[start_time][end_time][element_name] = parameter_str

    return simplified_data

def get_current_weather(simplified_data):
    try:
        # 獲取當前的日期和時間
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 遍歷所有的時間段
        for start_time in simplified_data:
            if start_time == 'location':
                continue
            for end_time in simplified_data[start_time]:
                # 如果當前時間在這個時間段內，則返回對應的天氣資訊
                if start_time <= now <= end_time:
                    return simplified_data[start_time][end_time]
                else:
                    # 如果沒有找到符合的時間段，則返回第一個天氣資訊
                    return simplified_data[start_time][end_time]
    except Exception as e:
        print(f"An error occurred: {e}")

    # 如果沒有找到任何天氣資訊，則返回None
    return None

# weather_data = get_weather_data(CITY)
# simplified_data = simplify_data(weather_data)
# current_weather = get_current_weather(simplified_data)

# print('The Data is: ' + str(current_weather))
# if current_weather is not None:
#     text = f'位置: {CITY}<br>天氣概況: {current_weather["Wx"]}<br>降雨機率: {current_weather["PoP"]}<br>體感: {current_weather["CI"]}'

# print(text)