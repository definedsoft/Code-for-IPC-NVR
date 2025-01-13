# 現在のアラームステータスを取得する
import requests

# NVR IP アドレス、ユーザー名、パスワード
nvr_ip = "192.168.1.15"
nvr_username = "admin"
nvr_password = "Admin123" 

url = f"http://{nvr_ip}/cgi-bin/alarm.cgi?userName={nvr_username}&password={nvr_password}&action=get&type=currentAlarmStatus"

response = requests.request("GET", url, timeout=3)

print(response.text)

'''
Not Find AlarmInfo
'''