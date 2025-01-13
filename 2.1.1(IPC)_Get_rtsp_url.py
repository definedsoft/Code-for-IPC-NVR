# RTSP の URL を取得し、この URL を使用して RTSP ライブ ビデオを取得します。
import requests

# カメラの IP アドレス、ユーザー名、パスワード
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

# camera_ip = "192.168.1.88"
# camera_username = "admin"
# camera_password = "admin"

# streamID=1  メインストリーム
# streamID=2  サブストリーム
streamID = 1
url = f"http://{camera_ip}/cgi-bin/video.cgi?type=RTSP&cameraID=1&streamID={streamID}"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print("response:",response)
if response.status_code == 200:
    res = response.text
    # rtsp://192.168.1.109:554/snl/live/1/1/TPvJ5dg=-bPvJ5dhs4PU=
    if res.startswith("rtsp"):
        print(res)
        rtsp_url = res.replace(camera_ip,f"{camera_username}:{camera_password}@{camera_ip}")
        print("rtsp_url:",rtsp_url)
    
    # response: <Response [200]>
    # response.text: Error,return=-402
    else:
        print("response.text:",response.text)


''' OK
response: <Response [200]>
rtsp://192.168.1.109:554/snl/live/1/1/-
rtsp_url: rtsp://admin:Admin123@192.168.1.109:554/snl/live/1/1/-
'''


''' NG
response: <Response [401]>

Error,return=-508
'''