# ポートリストを取得する
import requests

# NVR IP アドレス、ユーザー名、パスワード
nvr_ip = "192.168.1.15"
nvr_username = "admin"
nvr_password = "Admin123" 

url = f"http://{nvr_ip}/cgi-bin/param.cgi?userName={nvr_username}&password={nvr_password}&action=get&type=devicePort"

response = requests.request("GET", url, timeout=3)

print(response.text)

'''
clientPort=30001
httpPort=80
dataPort=554
httpsPort=443
'''