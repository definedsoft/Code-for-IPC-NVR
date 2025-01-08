# IPC CGI APIコード
# 機能：疎通確認



import subprocess

# 目標IP
hosts = ["192.168.1.1","192.168.1.18","192.168.1.200"]

for host in hosts:
    res = subprocess.run(["ping",host,"-c","2", "-W", "300"],stdout=subprocess.PIPE)
    # 引数の-cは疎通確認を行う回数指定です。
    # その次の引数の２が実際の回数になります。

    # 引数-Wはタイムアウトの指定です。
    # 小文字だとエラーになるので注意です。
    # その次の引数の３００が実際のタイムアウトの数値です。
    # ミリ秒単位で指定します。

    print(res.stdout.decode("cp932"))
    
    if res.returncode == 0 :
        print("成功\n\n")
    else:
        print("失敗\n\n")
    print("-----------------------------")




'''
# 実施結果

PING 192.168.1.1 (192.168.1.1) 56(84) bytes of data.
64 bytes from 192.168.1.1: icmp_seq=1 ttl=64 time=0.358 ms
64 bytes from 192.168.1.1: icmp_seq=2 ttl=64 time=0.342 ms

--- 192.168.1.1 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1011ms
rtt min/avg/max/mdev = 0.342/0.350/0.358/0.008 ms

成功


-----------------------------
PING 192.168.1.18 (192.168.1.18) 56(84) bytes of data.
From 192.168.1.103 icmp_seq=1 Destination Host Unreachable
From 192.168.1.103 icmp_seq=2 Destination Host Unreachable

--- 192.168.1.18 ping statistics ---
2 packets transmitted, 0 received, +2 errors, 100% packet loss, time 1012ms
pipe 2

失敗


-----------------------------
PING 192.168.1.200 (192.168.1.200) 56(84) bytes of data.
From 192.168.1.103 icmp_seq=1 Destination Host Unreachable
From 192.168.1.103 icmp_seq=2 Destination Host Unreachable

--- 192.168.1.200 ping statistics ---
2 packets transmitted, 0 received, +2 errors, 100% packet loss, time 1020ms
pipe 2

失敗


-----------------------------

'''
