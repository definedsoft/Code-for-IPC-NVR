# チャネル情報を取得する
import requests

# NVR IP アドレス、ユーザー名、パスワード
nvr_ip = "192.168.1.15"
nvr_username = "admin"
nvr_password = "Admin123" 

url = f"http://{nvr_ip}/cgi-bin/param.cgi?userName={nvr_username}&password={nvr_password}&action=get&type=channelInfo"

response = requests.request("GET", url, timeout=3)

print(response.text)

'''
channelNum=16
channelBinded=5
channelBegin=1
channelId=1
channelName=02.ä»£ç¨Camera
channelModel=SN-IPR8056DQAN-VZ2.7-12-23
channelFirmware=v3.6.1615.1006.3.0.2.16.0
channelHardware=V270034_20
channelStatus=5
channelProtocol=2
channelType=18
streamNum=2
streamBegin=1
streamId=1
streamEncoder=1
streamWidth=2592
streamHeight=1944
next_streamURL=2
streamId=2
streamEncoder=1
streamWidth=704
streamHeight=480
streamEnd=2
next_channelURL=2
channelId=3
channelName=04.å¨æ¿
channelModel=SN-TPC2553DRT-F3.5-23
channelFirmware=v3.6.1305.1006.3.0.8.8.0
channelHardware=V280072_5
channelStatus=5
channelProtocol=2
channelType=17
streamNum=2
streamBegin=1
streamId=1
streamEncoder=1
streamWidth=2880
streamHeight=1620
next_streamURL=2
streamId=2
streamEncoder=1
streamWidth=704
streamHeight=480
streamEnd=2
next_channelURL=3
channelId=5
channelName=07.èªè»¢è»
channelModel=
channelFirmware=
channelHardware=
channelStatus=5
channelProtocol=101
channelType=0
streamNum=2
streamBegin=1
streamId=1
streamEncoder=1
streamWidth=1920
streamHeight=1080
next_streamURL=2
streamId=2
streamEncoder=2
streamWidth=1920
streamHeight=1080
streamEnd=2
next_channelURL=4
channelId=6
channelName=05.å¨æ¿Thermal
channelModel=SN-TPC2553DRT-F3.5-23
channelFirmware=v3.6.1305.1006.3.0.8.8.0
channelHardware=V280072_5
channelStatus=5
channelProtocol=2
channelType=17
streamNum=2
streamBegin=1
streamId=1
streamEncoder=1
streamWidth=704
streamHeight=480
next_streamURL=2
streamId=2
streamEncoder=1
streamWidth=704
streamHeight=480
streamEnd=2
next_channelURL=5
channelId=7
channelName=7
channelModel=SN-IPR8050DQAA-Z2.7-13.5-23
channelFirmware=v3.6.1602.1006.1.97.18.2.5
channelHardware=V210014_73
channelStatus=5
channelProtocol=2
channelType=18
streamNum=2
streamBegin=1
streamId=1
streamEncoder=1
streamWidth=2592
streamHeight=1944
next_streamURL=2
streamId=2
streamEncoder=1
streamWidth=704
streamHeight=480
streamEnd=2
channelEnd=5
'''