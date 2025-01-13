# 露出パラメータを取得する
import requests

# カメラの IP アドレス、ユーザー名、パスワード
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

url = f"http://{camera_ip}/cgi-bin/sensor.cgi?cameraID=1&schemeID=0&action=get&type=Exposure"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.text)

'''
exposureMode=0      # 0: Automatic, 1: Manual, 2: Shutter priority
                    # 0: 自動, 1: 手動, 2: シャッター優先
shutter=8           # 2: 1/15, 3: 1/10, 4: 1/12.5, 5: 1/15, 6: 1/20, 7: 1/25, 8: 1/30, 9: 1/50, 
                    # 11: 1/100, 13: 1/125, 14: 1/150, 15: 1/200, 16: 1/250, 17: 1/500, 18: 1/1000, 19: 1/2000, 
                    # 20: 1/5000, 21: 1/10000, 22: 1/20000
meterArea=4         # 4: Global, 0: Center point, 1: Central area
                    # 4: グローバル, 0: 中心点, 1: 中央エリア
gain=50
'''