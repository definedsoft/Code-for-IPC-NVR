# スナップショットパラメータを取得する
import requests

# カメラの IP アドレス、ユーザー名、パスワード
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

url = f"http://{camera_ip}/cgi-bin/param.cgi?action=get&type=snapshot&cameraID=1&streamID=1"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.text)

'''
ChannelID=1
SnapshotResolution=4608x1728
SnapshotQuality=9               # 画質 1: Low, 5: Medium, 9: High
'''