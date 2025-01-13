# デバイス情報を取得する
import requests

# カメラの IP アドレス
camera_ip = "192.168.1.109"

url = f"http://{camera_ip}/cgi-bin/param.cgi?action=get&type=deviceInfo"

# デバイス情報を取得する時、認証は不要
response = requests.request("GET", url, timeout=3)

print(response.text)

'''
deviceID=21BAxxx
deviceName=
deviceType=22
productModel=SN-IPP8085QAS-B2.8-23
manufacturerID=003
manufacturerName=IPCamera
MACAddress=00:1C:27:XX:XX:XX
hardwareVer=V330014_1
softwareVer=v5.0.1621.1006.3.0.2.0.0
channelNum=1
alarmInNum=1
alarmOutNum=1
RS485Num=0
ubootVersion=v6.4
kerneVersion=v6.4_20240821
networkCardNum=1
'''