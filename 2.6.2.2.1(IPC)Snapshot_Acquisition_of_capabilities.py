# スナップショット機能の取得
import requests

# カメラの IP アドレス、ユーザー名、パスワード
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

url = f"http://{camera_ip}/cgi-bin/param.cgi?action=get&type=snapshotAbility"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.text)

'''
resolutionCount=4
resolutionBegin=1
resolution=4608x1728
next_ResolutionURL=2
resolution=3072x1152
next_ResolutionURL=3
resolution=1536x576
next_ResolutionURL=4
resolution=960x360
resolutionEnd=1
qualityCount=3
qualityBegin=1
quality=1
next_QualityURL=2
quality=5
next_QualityURL=3
quality=9
qualityEnd=1
'''