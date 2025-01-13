# # デバイス情報を取得する
import requests

# NVR IP アドレス、ユーザー名、パスワード
nvr_ip = "192.168.1.15"
nvr_username = "admin"
nvr_password = ""         # パスワードが任意

url = f"http://{nvr_ip}/cgi-bin/param.cgi?action=get&type=deviceInfo&userName={nvr_username}&password={nvr_password}"

# デバイス情報を取得する時、認証は不要
response = requests.request("GET", url, timeout=3)

print(response.text)

'''
deviceID=5002xxxx
deviceType=5                  # IPカメラ(default is 1), NVR(default is 5)
deviceName=B011003ACxxxxxx
softwareVer=v4.7.1625.0000.003.0.1.23.0
hardwareVer=50021008
manufacturerID=NVR3908E2-P8-JA
MACAddress=00:1C:27:xx:xx:xx
sn=B011003ACxxxxxx
ubootVer=18040811361C
kernelVer=18040811301C
channelNum=8
hddNum=2
alarmInNum=6
alarmOutNum=2
audioInNum=1
audioOutNum=1
RS485Num=1
'''