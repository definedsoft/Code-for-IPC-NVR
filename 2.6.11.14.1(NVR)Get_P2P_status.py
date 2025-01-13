# P2Pステータスを取得する
import requests

# NVR IP アドレス、ユーザー名、パスワード
nvr_ip = "192.168.1.15"
nvr_username = "admin"
nvr_password = "Admin123" 

url = f"http://{nvr_ip}/cgi-bin/param.cgi?userName={nvr_username}&password={nvr_password}&action=get&type=p2p"

response = requests.request("GET", url, timeout=3)

print(response.text)

'''
enable=1          # 0: Offline, 1: Online
'''