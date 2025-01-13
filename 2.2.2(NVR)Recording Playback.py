# 録画をダウンロードする
import requests

# NVR IP アドレス、ユーザー名、パスワード
nvr_ip = "192.168.1.15"
nvr_username = "admin"
nvr_password = "Admin123"

camera_id = "1"
stream_id = "1"                 # 1:メインストリーム、2:サブストリーム
start_time = "20241230170410"   # YYYYMMDDHHMMSS
end_time = "20241230170430"

url = f"http://{nvr_ip}/cgi-bin/record.cgi?userName={nvr_username}&password={nvr_password}&action=playBack&cameraID={camera_id}&streamID={stream_id}&startTime={start_time}&endTime={end_time}"


response = requests.request("GET", url)

# 応答内容を文書に保存する
response_file = f'{nvr_ip}_{camera_id}_{stream_id}_{start_time}-{end_time}.txt'
with open(response_file, "wb+") as f:
    f.write(response.content)

# print(response.text)
# 応答コンテンツを分割する
lines = response.content.split(b'\r\n')

# 境界文字列を定義する
boundary = b'--myboundary'

# 変数を初期化してバイナリコンテンツを保存する
binary_data = b''

# バイナリコンテンツセクションに到達したかどうかをマークします
binary_section_started = False

# バイナリコンテンツをファイルに保存
h264_file = f'{nvr_ip}_{camera_id}_{stream_id}_{start_time}-{end_time}.h264'
with open(h264_file, 'wb+') as f:

    for line in lines:
        # 判断是否到达二进制内容部分
        if binary_section_started:
            binary_data += line + b'\r\n'
        elif line == boundary:
            # 遇到边界标志
            binary_section_started = False

            # # 保存二进制内容到文件
            # f.write(binary_data)

        elif line == b'':
            # 遇到空行
            binary_section_started = True

    # 去掉末尾多余的回车换行
    binary_data = binary_data.rstrip(b'\r\n')

    f.write(binary_data)

print(f'Video saved to {h264_file}')




# MP4ファイルに変換する
import subprocess
mp4_file = f'{nvr_ip}_{camera_id}_{stream_id}_{start_time}-{end_time}.mp4'
subprocess.run(['ffmpeg', '-i', h264_file, '-c', 'copy', mp4_file])

print("MP4 saved to: ", mp4_file)





# 保存した臨時ファイルを削除する
import os
os.remove(response_file)
os.remove(h264_file)
