import requests

url = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWA-3FB7ACCF-6A57-4021-9348-D1A14CFBBC65&locationName=%E6%96%B0%E5%8C%97%E5%B8%82'

data = requests.get(url)   # 取得 JSON 檔案的內容為文字
data_json = data.json()    # 轉換成 JSON 格式
location = data_json['records']['location']  # 取出 location 的內容
for i in location:
    city = i['locationName']    # 縣市名稱
    wx8 = i['weatherElement'][0]['time'][0]['parameter']['parameterName']    # 天氣現象
    maxt8 = i['weatherElement'][1]['time'][0]['parameter']['parameterName']  # 最高溫
    mint8 = i['weatherElement'][2]['time'][0]['parameter']['parameterName']  # 最低溫
    ci8 = i['weatherElement'][3]['time'][0]['parameter']['parameterName']    # 舒適度
    pop8 = i['weatherElement'][4]['time'][0]['parameter']['parameterName']   # 降雨機率
    print(f'{city}未來 8 小時{wx8}，最高溫 {maxt8} 度，最低溫 {mint8} 度，降雨機率 {pop8} %')