# IPCからスナップショットイメージを取得する
import requests
from datetime import datetime

# カメラの IP アドレス
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

# quality=1~9、　　　1最高画質   9低画質
quality = 1
url = f"http://{camera_ip}/cgi-bin/image.cgi?cameraID=1&quality={quality}"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.status_code)
if response.status_code == 200:
    res = response.content
    # print(res)

    # 画像を保存, 保存ファイル名は時間+カメラの IP アドレス.jpg
    # 現在の日時を取得
    timestamp = datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
    filename = f"{timestamp}_{camera_ip}_snapshot.jpg"
    print(filename)
    with open(filename, "wb") as f:
        f.write(res)
else:
    print("Error")