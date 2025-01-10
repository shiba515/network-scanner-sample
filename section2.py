from scapy.all import IP, ICMP, sr1


with open("arp_alive_list_copy.txt", 'r') as file:
    ip_list = [line.strip() for line in file if line.strip()]

for ip in ip_list:
    packet = IP(dst=ip)/ICMP() # 宛先IPにICMPパケットを設定
    response = sr1(packet, timeout=1, verbose=0)  # パケットを送信し、応答を待つ
    if response:
        print(f"{ip} is up")
    else:
        print(f"{ip} is down")

