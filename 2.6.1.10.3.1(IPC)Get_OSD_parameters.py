# OSDパラメータを取得する
import requests

# カメラの IP アドレス、ユーザー名、パスワード
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

url = f"http://{camera_ip}/cgi-bin/param.cgi?action=get&type=OSD&cameraID=1"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.text)

'''
fontColor=2
TwelveHoursFlag=0    <-- 0:24時間制, 1:12時間制
WeekFlag=1
alpha=4         <-- 透明度
'''



'''
font color
0: Other
1: White
2: Black
3: Red
4: Orange
5: Yellow
6: Green
7: Blue
8: Blue
9: Purple

0: その他
1: 白
2: 黒
3: 赤
4: オレンジ
5: 黄
6: 緑
7: 青
8: 青
9: 紫
'''

'''
transparency 透明度
0: Other
1: Transparent
2: Translucent
3: Semi-translucent
4: Opaque

0: その他
1: 透明
2: 半透明
3: 半透明
4: 不透明
'''