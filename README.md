# Transparent Screen Weather Clock

這是一個使用透明 LCD 和 Raspberry Pi 製作的未來感天氣時鐘展示專案。使用 Flask + HTML/CSS 前端，配合透明螢幕的透光特性，呈現黑白分明、極簡風的顯示效果。

## ✨ 功能特色

- 顯示目前時間（時／分／秒字型大小遞減）
- 顯示目前天氣概況（中央氣象局資料）
- 使用七段數位風格字型（DSEG7）
- 適用透明 LCD 螢幕，可顯示在玻璃上
- 支援 Raspberry Pi 自動啟動＋全螢幕 kiosk 模式

---

## 🚀 安裝與執行（for Raspberry Pi）

### 1. 複製專案到 Raspberry Pi

```bash
git clone YOUR_REPO
cd tablecloth-v1/tarnsparent_screan
```

### 2. 安裝依賴與設定

```bash
chmod +x install_pi_setup.sh start.sh
./install_pi_setup.sh
```

### 3. 測試啟動

```bash
./start.sh
```

執行過程中會自動記錄 log 到 `flask.log`，以利除錯。

---

## 🔧 開機自動啟動與全螢幕模式

### 1. 將自動啟動檔放入 autostart 資料夾

```bash
mkdir -p ~/.config/autostart
cp kiosk.desktop ~/.config/autostart/
```

開機後將自動啟動 Flask 並以 Chromium kiosk 模式全螢幕打開畫面。

---

## 🌤️ API 金鑰設定

請在專案根目錄放置 `.env` 檔案，格式如下：

```env
KEY=你的中央氣象局 API 金鑰
LOCATION=新北市
```

---

## 📁 專案結構摘要

```hss
tarnsparent_screan/
├── app.py               # Flask 主伺服器
├── UI.html              # 前端畫面
├── weather.py           # 抓取氣象資料
├── fonts/               # 自定七段數字字型
├── .env                 # API 金鑰與城市設定
├── start.sh             # 啟動伺服器腳本
├── install_pi_setup.sh  # Pi 初始設定腳本
├── kiosk.desktop        # 自動啟動 + 全螢幕
├── requirements.txt     # 套件清單
```

---

## 🪪 License

MIT

## 📦 專案打包

若需將整個專案打包，可使用以下指令：

```bash
tar --exclude="venv" --exclude="__pycache__" -czf transparent_display.tar.gz tarnsparent_screan
```

此壓縮檔可方便移轉或備份（不包含虛擬環境與快取）。
