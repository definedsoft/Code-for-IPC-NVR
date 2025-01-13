# OSD機能を取得する
import requests

# カメラの IP アドレス、ユーザー名、パスワード
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

url = f"http://{camera_ip}/cgi-bin/param.cgi?action=get&type=OSDAbility"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.text)


'''
maxCanvasProperNum=8
maxOSDNum=1
osdTypeCount=5
osdTypeBegin=1
osdType=1
next_OSDTypeURL=2
osdType=2
next_OSDTypeURL=3
osdType=3
next_OSDTypeURL=4
osdType=4
next_OSDTypeURL=5
osdType=5
osdTypeEnd=1
fontSizeCount=3
fontSizeBegin=1
fontSize=3
next_FontSizeURL=2
fontSize=2
next_FontSizeURL=3
fontSize=1
fontSizeEnd=1
timeFormatCount=6
timeFormatBegin=1
timeFormat=YYYY-MM-DDhh:mm:ssww
next_TimeURL=2
timeFormat=hh:mm:ssYYYY-MM-DDww
next_TimeURL=3
timeFormat=MM/DD/YYYYhh:mm:ssww
next_TimeURL=4
timeFormat=hh:mm:ssMM/DD/YYYYww
next_TimeURL=5
timeFormat=DD/MM/YYYYhh:mm:ssww
next_TimeURL=6
timeFormat=hh:mm:ssDD/MM/YYYYww
timeFormatEnd=1
fontAlphaCount=4
fontAlphaBegin=1
fontAlpha=1
next_AlphaURL=2
fontAlpha=2
next_AlphaURL=3
fontAlpha=3
next_AlphaURL=4
fontAlpha=4
fontAlphaEnd=1
supportFontColor=1
allFontColor=1
supportFontInverse=0
'''

'''
OSD Type
OSD Type                               
1: Device name							1: デバイス名
2: Camera number						2: カメラ番号
3: Camera name							3: カメラ名
4: Time watermark						4: 時刻ウォーターマーク
5: Text watermark						5: テキスト ウォーターマーク
6: PTZ position operation watermark		6: PTZ 位置操作ウォーターマーク
7: PTZ behavior operation watermark		7: PTZ 動作操作ウォーターマーク
8: PTZ temperature						8: PTZ 温度
'''