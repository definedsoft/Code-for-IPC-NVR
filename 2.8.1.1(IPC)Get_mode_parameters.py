# (フロントエンド)モードパラメータの取得
import requests

# カメラの IP アドレス、ユーザー名、パスワード
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

url = f"http://{camera_ip}/cgi-bin/sensor.cgi?action=get&type=sensorMode&cameraID=1"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.text)

'''
switchMode=0        # 0:None 1:Time Mode
beginHour=0
beginMinute=0
endHour=24
endMinute=0
'''
