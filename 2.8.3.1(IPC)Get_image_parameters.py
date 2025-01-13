# (フロントエンド)画像パラメータを取得する
import requests

# カメラの IP アドレス、ユーザー名、パスワード
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

url = f"http://{camera_ip}/cgi-bin/sensor.cgi?cameraID=1&type=imaging&schemeID=0&action=get"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.text)

'''
brightness=50
saturation=50
sharpness=50
contrast=50
'''