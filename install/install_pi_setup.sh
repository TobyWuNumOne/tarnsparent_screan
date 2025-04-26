#!/bin/bash

echo "🔧 安裝系統必要套件..."
sudo apt update
sudo apt install -y python3-venv python3-pip unclutter chromium-browser xdotool

echo "📦 建立虛擬環境並安裝依賴..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

echo "✔️ 初始化完成！"
echo "👉 執行 ./start.sh 開始伺服器"