# デバイスの時刻を取得する
import requests

# NVR IP アドレス、ユーザー名、パスワード
nvr_ip = "192.168.1.15"
nvr_username = "admin"
nvr_password = "Admin123" 

url = f"http://{nvr_ip}/cgi-bin/param.cgi?userName={nvr_username}&password={nvr_password}&action=get&type=dateTime"

response = requests.request("GET", url, timeout=3)

print(response.text)

'''
datefmt=0  # 0: YY/MM/DD hh:mm:ss, 1: hh:mm:ss YY/MM/DD, 2: MM/DD/YY hh:mm:ss, 
           # 3: hh:mm:ss MM/DD/YY, 4: DD/MM/YY hh:mm:ss, 5: hh:mm:ss DD/MM/YY
timefmt=1  # 0: 12H, 1: 24H
year=2025
month=1
day=13
hour=17
minute=43
second=15
'''