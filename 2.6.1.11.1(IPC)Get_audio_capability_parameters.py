# オーディオ機能パラメータを取得する
import requests

# カメラの IP アドレス、ユーザー名、パスワード
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

url = f"http://{camera_ip}/cgi-bin/param.cgi?action=get&cameraID=1&type=audioAbility"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.text)

'''
audioInCount=2
audioInBegin=2
audioInType=1       # Audio input type: 1: Built-in, 2: External, 3: Line input, 4: Differential line input, 5: Dual input
                    # オーディオ入力タイプ: 1: 内蔵, 2: 外部, 3: ライン入力, 4: 差動ライン入力, 5: デュアル入力
next_AudioInURL=2
audioInType=3
audioInEnd=2
audioOutCount=2
audioOutBegin=2
audioOutType=2      # Audio output type: 0: Automatic, 1: External, 2: Built-in
                    # オーディオ出力タイプ: 0: 自動, 1: 外部, 2: 内蔵
next_AudioOutURL=2
audioOutType=1
audioOutEnd=2
audioVolumeMin=0
audioVolumeMax=100
'''