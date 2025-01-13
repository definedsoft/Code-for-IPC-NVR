# (フロントエンド)ノイズ低減パラメータを取得する
import requests

# カメラの IP アドレス、ユーザー名、パスワード
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

url = f"http://{camera_ip}/cgi-bin/sensor.cgi?cameraID=1&type=NoiseReduction&schemeID=3&action=get"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.text)

'''
2DNR=1                  # 0:close, 1:open
3DNR=1                  # 0:close, 1:open
2DNRMode=1              # 1:Auto, 2:Manual
3DNRMode=1              # 1:Auto, 2:Manual
2DNRMaxStrength=50
3DNRMaxStrength=50
2DNRFixedStrength=50
3DNRFixedStrength=50
'''