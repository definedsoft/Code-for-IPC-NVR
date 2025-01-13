# プロトコル情報パラメータを取得する
import requests

# カメラの IP アドレス、ユーザー名、パスワード
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

url = f"http://{camera_ip}/cgi-bin/param.cgi?action=get&type=protocolInfo"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.text)

'''
protocolName=ONVIF
protocolVersion=v22.06
protocolSoftwareVersion=v22.06_build000581
rtspRule=rtsp://ip:port/snl/live/cameraid/streamid
rtspExample=rtsp://192.168.1.109:554/snl/live/1/1
onvifUuid=483673c0-a403-11ef-b078-001c2721ba1c
'''
