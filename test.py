from dotenv import load_dotenv, dotenv_values
from pathlib import Path
import os

dotenv_path = Path(__file__).parent / ".env"
print(f"使用的 dotenv 路徑: {dotenv_path.resolve()}")

# 顯示 dotenv 裡實際讀到的值（這不經過 os.environ）
config = dotenv_values(dotenv_path)
print("dotenv_values() 讀到的內容：", config)

# 嘗試載入到 os.environ
load_dotenv(dotenv_path=dotenv_path.resolve())

# 再印 os.environ 確認
print("os.environ 中的 API_KEY：", os.environ.get('KEY'))

# 最後再用 getenv() 印一次
api_key = os.getenv('KEY')
print("os.getenv() 拿到的 API_KEY：", api_key)