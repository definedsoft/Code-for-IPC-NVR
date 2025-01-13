# デバイスのタイムゾーンパラメータを取得する
import requests

# カメラの IP アドレス、ユーザー名、パスワード
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

url = f"http://{camera_ip}/cgi-bin/param.cgi?action=get&type=timeZone"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.text)


'''
timeZone=235              <-- (GMT+09:00) Osaka, Sapporo, Tokyo
DSTOpenFlag=0
beginMonth=3
beginWeekly=5
beginWeekDays=0
beginTime=60
endMonth=10
endWeekly=5
endWeekDays=0
endTime=120
'''
