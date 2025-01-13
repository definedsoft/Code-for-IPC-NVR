# 録画ポリシーの取得する
import requests

# NVR IP アドレス、ユーザー名、パスワード
nvr_ip = "192.168.1.15"
nvr_username = "admin"
nvr_password = "Admin123"

camera_ID = 1

url = f"http://{nvr_ip}/cgi-bin/param.cgi?userName={nvr_username}&password={nvr_password}&action=get&type=recordPolicy&cameraID={camera_ID}"

response = requests.request("GET", url, timeout=3)

print(response.text)

'''
cameraID=1
RecordOpenFlag=1
AudioOpenFlag=0
weekDayBegin=1
weekDay=0
startTime=0
endTime=86400
next_weekDayURL=2
weekDay=1
startTime=0
endTime=86400
next_weekDayURL=3
weekDay=2
startTime=0
endTime=86400
next_weekDayURL=4
weekDay=3
startTime=0
endTime=86400
next_weekDayURL=5
weekDay=4
startTime=0
endTime=86400
next_weekDayURL=6
weekDay=5
startTime=0
endTime=86400
next_weekDayURL=7
weekDay=6
startTime=0
endTime=86400
weekDayEnd=7
'''