# 録画検索する
import requests

# NVR IP アドレス、ユーザー名、パスワード
nvr_ip = "192.168.1.15"
nvr_username = "admin"
nvr_password = "Admin123"

camera_id = "1"
start_time = "20241230170410"   # YYYYMMDDHHMMSS
end_time = "20241230170510"

url = f"http://{nvr_ip}/cgi-bin/record.cgi?userName={nvr_username}&password={nvr_password}&action=query&cameraID={camera_id}&startTime={start_time}&endTime={end_time}"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload, timeout=3)

print(response.text)


'''
resultCount=1
resultBegin=1
startTime=20241230170400
endTime=20241230170600
resultEnd=1
'''
