# カメラパラメータ(周波数)を取得する
import requests

# カメラの IP アドレス、ユーザー名、パスワード
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

url = f"http://{camera_ip}/cgi-bin/param.cgi?action=get&cameraID=1&type=videoSystem"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.text)


'''
videoFormat=0        <-- 0:NTSC, 1:PAL
frequency=60
'''