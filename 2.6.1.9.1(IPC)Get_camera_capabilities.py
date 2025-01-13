# カメラ機能を取得する
import requests

# カメラの IP アドレス、ユーザー名、パスワード
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

url = f"http://{camera_ip}/cgi-bin/param.cgi?action=get&type=videoSystemAbility"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.text)


'''
videoFormatCount=2        <-- 0:NTSC, 1:PAL
videoFormatBegin=1
videoFormat=1
frequencyCount=1
frequencyBegin=1
frequency=50
frequencyEnd=1
next_FormatURL=2
videoFormat=0
frequencyCount=1
frequencyBegin=1
frequency=60
frequencyEnd=1
videoFormatEnd=1
'''