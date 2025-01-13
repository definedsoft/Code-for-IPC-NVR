# マルチキャストパラメータを取得する
import requests

# カメラの IP アドレス、ユーザー名、パスワード
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

url = f"http://{camera_ip}/cgi-bin/param.cgi?action=get&type=multicastParameters"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.text)

'''
channelCount=1
channelBegin=1
channelId=1
streamCount=2
streamBegin=1
streamId=1
videoAddress=238.255.255.255
videoPort=25330
audioAddress=238.255.255.255
audioPort=25430
sourceAddress=238.255.255.255
sourcePort=25530
next_StreamURL=2
streamId=2
videoAddress=238.255.255.255
videoPort=25340
audioAddress=238.255.255.255
audioPort=25440
sourceAddress=238.255.255.255
sourcePort=25540
streamEnd=2
channelEnd=1
'''