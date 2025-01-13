# シーンモードを取得する
import requests

# カメラの IP アドレス、ユーザー名、パスワード
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

url = f"http://{camera_ip}/cgi-bin/sensor.cgi?action=get&type=SceneMode&cameraID=1&schemeID=3"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.text)

'''
Scene=1         # 0: Indoor 1: Outdoor
CorridorMode=0  # 廊下モード 0: Close 1: Open
'''