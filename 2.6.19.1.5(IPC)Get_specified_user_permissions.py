# 指定ユーザー権限を取得する
import requests

# カメラの IP アドレス、ユーザー名、パスワード
camera_ip = "192.168.1.109"
camera_username = "admin"
camera_password = "Admin123"

url = f"http://{camera_ip}/cgi-bin/param.cgi?type=User&action=getUserPrivileges&user=admin"

# Auth Type:Digest Auth MD5
response = requests.request("GET", url, auth=(camera_username, camera_password), timeout=3)

print(response.text)

'''
privilegeCount=15
privilegeBegin=1
privilege=0
next_privilegeURL=2
privilege=1
next_privilegeURL=3
privilege=2
next_privilegeURL=4
privilege=3
next_privilegeURL=5
privilege=4
next_privilegeURL=6
privilege=5
next_privilegeURL=7
privilege=6
next_privilegeURL=8
privilege=7
next_privilegeURL=9
privilege=8
next_privilegeURL=10
privilege=10
next_privilegeURL=11
privilege=11
next_privilegeURL=12
privilege=12
next_privilegeURL=13
privilege=13
next_privilegeURL=14
privilege=14
next_privilegeURL=15
privilege=16
privilegeEnd=1
'''


'''
Permissions
0: Real-time video
1: Video Control
2: PTZ control
3: Audio
4: Video playback
5: Backup
6: Manual recording
7: Video recording strategy
8: Disk Management
9: Alarm retrieval
10: Device Management
11: Permission Management
12: Parameter configuration
13: Video maintenance
14: Log
15: Infrared thermal imaging
16: Intelligent Detection

0: リアルタイムビデオ
1: ビデオコントロール
2: PTZ コントロール
3: オーディオ
4: ビデオ再生
5: バックアップ
6: 手動録画
7: ビデオ録画戦略
8: ディスク管理
9: アラーム取得
10: デバイス管理
11: 権限管理
12: パラメータ設定
13: ビデオメンテナンス
14: ログ
15: 赤外線サーマルイメージング
16: インテリジェント検出
'''