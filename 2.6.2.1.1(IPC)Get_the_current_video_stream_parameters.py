# ビデオストリームパラメータを取得する
import requests

# カメラの IP アドレス、ユーザー名、パスワード
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

url = f"http://{camera_ip}/cgi-bin/param.cgi?action=get&type=AVStream&cameraID=1&streamID=1"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.text)

'''
streamName=stream1
videoEncoderType=8     <-- 1: H264, 2: MJPEG, 4: H264_MAIN, 5: H264_HIGH, 8: H265_MAIN
videoEncoderLevel=2    <-- 1: Low, 2: Medium, 3: High
audioEncoderType=102   <-- 102:G711_Alaw, 103:G711_Ulaw, 107:ARM, 108:PCM, 109:NONE
resolution=4608*1728
frameRate=15
iFrameInterval=30
bitRateType=1          <-- 1: CBR, 2: VBR
bitRate=8192
streamEncoderFlag=0
'''