# デバイスのタイムゾーンパラメータを取得する
import requests

# NVR IP アドレス、ユーザー名、パスワード
nvr_ip = "192.168.1.15"
nvr_username = "admin"
nvr_password = "Admin123" 

url = f"http://{nvr_ip}/cgi-bin/param.cgi?userName={nvr_username}&password={nvr_password}&action=get&type=timeZone"

response = requests.request("GET", url, timeout=3)

print(response.text)

'''
timeZone=230        <-- (GMT+09:00) Seoul, Tokyo, Osaka, Sapporo
DSTOpenFlag=0
beginMonth=3
beginWeekly=5
beginWeekDays=7
beginTime=60
endMonth=10
endWeekly=5
endWeekDays=7
endTime=60
offset=60
'''
