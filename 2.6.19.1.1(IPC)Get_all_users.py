# ユーザーリストを取得する
import requests

# カメラの IP アドレス、ユーザー名、パスワード
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

url = f"http://{camera_ip}/cgi-bin/param.cgi?action=getAllUser&type=User"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.text)

'''
userCount=1
userBegin=1
userName=admin
groupName=SuperAdmin
privilegeCount=15
privilegeBegin=1
privilege=0
next_privilegeURL=2
privilege=1
next_privilegeURL=3
privilege=2
next_privilegeURL=4
privilege=3
next_privilegeURL=5
privilege=4
next_privilegeURL=6
privilege=5
next_privilegeURL=7
privilege=6
next_privilegeURL=8
privilege=7
next_privilegeURL=9
privilege=8
next_privilegeURL=10
privilege=10
next_privilegeURL=11
privilege=11
next_privilegeURL=12
privilege=12
next_privilegeURL=13
privilege=13
next_privilegeURL=14
privilege=14
next_privilegeURL=15
privilege=16
privilegeEnd=1
userEnd=1
'''