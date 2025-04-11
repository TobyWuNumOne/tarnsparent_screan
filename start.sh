#!/bin/bash
cd "$(dirname "$0")"           # 切換到這個腳本所在資料夾（也就是你的專案資料夾）
source venv/bin/activate       # 啟動虛擬環境
echo "---- $(date) 啟動 Flask ----" >> flask.log
python app.py >> flask.log 2>&1  # 執行 Flask 應用