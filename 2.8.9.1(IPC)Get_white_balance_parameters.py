# (フロントエンド)ホワイトバランスパラメータを取得する
import requests

# カメラの IP アドレス、ユーザー名、パスワード
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"


url = f"http://{camera_ip}/cgi-bin/sensor.cgi?cameraID=1&type=WBMode&action=get"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.text)

'''
wbMode=0      # 0: Auto, 1: Tungsten, 2: Fluorescent, 3: Daylight, 4: Shadow, 9: Manual
              # 0: 自動, 1: 白熱灯, 2: 蛍光灯, 3: 日光, 4: 影, 9: 手動
redGain=0
blueGain=0
'''