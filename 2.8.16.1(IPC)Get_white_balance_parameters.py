# (フロントエンド)ホワイトバランスパラメータを取得する
import requests

# カメラの IP アドレス、ユーザー名、パスワード
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

url = f"http://{camera_ip}/cgi-bin/sensor.cgi?action=get&type=whiteBalance&cameraID=1&schemeID=0"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.text)

'''
mode=0      # 0:Auto, 1:Tungsten, 2:Fluorescent, 3:Daylight, 4:Shadow
            # 0:オート, 1:白熱灯, 2:蛍光灯, 3:昼光, 4:影
redGain=0
blueGain=0
'''