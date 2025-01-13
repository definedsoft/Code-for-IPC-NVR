# ローカルネットワークパラメータを取得する
import requests

# カメラの IP アドレス、ユーザー名、パスワード
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

url = f"http://{camera_ip}/cgi-bin/param.cgi?action=get&type=localNetwork&IPProtoVer=1&netCardId=1"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.text)

'''
localNetworkBegin=1
IPProtoVer=1
netCardId=1
IPAddress=192.168.1.109
subNetmask=255.255.255.0
subGetway=192.168.1.1
preferredDNS=192.168.1.1
alternateDNS=
autoGetIPFlag=0
mtu=1500
localNetworkEnd=1
'''