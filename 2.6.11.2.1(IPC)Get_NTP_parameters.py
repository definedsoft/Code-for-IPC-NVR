# NTPパラメータを取得する
import requests

# カメラの IP アドレス、ユーザー名、パスワード
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

url = f"http://{camera_ip}/cgi-bin/param.cgi?action=get&type=NTP"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.text)

'''
enableFlag=1
IPProtoVer=1
NTPIP=ntp.nict.jp
NTPPort=123
NTPCheckTime=3600
'''