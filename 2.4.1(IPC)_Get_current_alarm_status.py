# IPC上、現在のアラームステータスを取得する
import requests

# カメラの IP アドレス
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

url = f"http://{camera_ip}/cgi-bin/alarm.cgi?action=get&type=currentAlarmStatus"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.text)


'''
Not Find AlarmInfo
'''