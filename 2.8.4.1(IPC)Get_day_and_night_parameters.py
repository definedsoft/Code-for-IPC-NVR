# 昼と夜の設定を取得する
import requests

# カメラの IP アドレス、ユーザー名、パスワード
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

url = f"http://{camera_ip}/cgi-bin/sensor.cgi?cameraID=1&schemeID=0&type=dayNight&action=get"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.text)

'''
dayNightMode=0              # 0: Automatic, 1: Day mode, 2: Night mode, 3: Timing
                            # 0: 自動, 1: 昼モード, 2: 夜モード, 3: タイミング
dayNightSensitivity=50
delay=5
lightMode=0
infrared=1
infraredIntensity=50
'''