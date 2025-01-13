# 録画ポリシーパラメータを取得する
import requests

# カメラの IP アドレス、ユーザー名、パスワード
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

url = f"http://{camera_ip}/cgi-bin/param.cgi?action=get&cameraID=1&type=recordPolicy"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.text)

'''
cameraID=1
RecordOpenFlag=0    # 0:録画停止 1:録画開始
SaveDays=0
StreamId=1
AudioOpenFlag=0     # 0:録音する 1:録音しない
DiskGroupId=1
PreRecordTime=10
'''
