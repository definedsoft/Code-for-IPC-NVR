# ローカルネットワークパラメータを取得する
import requests

# NVR IP アドレス、ユーザー名、パスワード
nvr_ip = "192.168.1.15"
nvr_username = "admin"
nvr_password = "Admin123" 

url = f"http://{nvr_ip}/cgi-bin/param.cgi?userName={nvr_username}&password={nvr_password}&action=get&type=localNetwork&IPProtoVer=1&netCardId=1"

response = requests.request("GET", url, timeout=3)

print(response.text)


'''
IPProtoVer=1
netCardId=1
DHCP=0
IPAddress=192.168.1.15
subNetmask=255.255.255.0
subGateway=192.168.1.1
autoGetIPFlag=0
preferredDNS=192.168.1.1
alternateDNS=
'''