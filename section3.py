from scapy.all import IP, TCP, sr1

# IPアドレスのリストを定義
ip_list = ["xxx.xxx.xxx.xxx", "xxx.xxx.xxx.xxx", "xxx.xxx.xxx.xxx"] #出力されたipアドレスを入力

# 各IPアドレスに対してTCP SYNスキャンを実行
for host in ip_list:
    ip_packet = IP(dst=host)
    tcp_syn = TCP(dport=80, flags="S")  # ポート80に対してSYNパケットを送信
    response = sr1(ip_packet/tcp_syn, timeout=2, verbose=0)

    if response and response.haslayer(TCP):
        if response.getlayer(TCP).flags == 0x12:  # SYN-ACKフラグがセットされている場合
            print(f"Host {host} is accepting TCP connections on port 80")
            # RSTを送信して接続を閉じる
            rst_packet = IP(dst=host)/TCP(dport=80, flags="R")
            sr1(rst_packet, timeout=1, verbose=0)
        else:
            print(f"Host {host} sent a TCP response, but not SYN-ACK")
    else:
        print(f"Host {host} did not respond to TCP SYN on port 80")
