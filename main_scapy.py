import ipaddress
from scapy.all import ARP, Ether, srp

network = ipaddress.ip_network("xxx.xxx.xxx.xxx/xx")
interface = "xxxx"  # 使用するインターフェース

print("Sending ARP requests...")
hosts = []
for ip in network.hosts():
    # ARPリクエストを送信する前にイーサネットフレームとARPパケットを生成
    ethernet_frame = Ether(dst="ff:ff:ff:ff:ff:ff")  # ブロードキャスト用MACアドレス
    arp_request = ARP(pdst=str(ip)) # ARPリクエスト

    answered, unanswered = srp(ethernet_frame/arp_request, timeout=2, iface=interface, verbose=0)
    for sent, received in answered:
        print(f"Host {received.psrc} ({received.hwsrc}) is up")
        hosts.append(received.psrc)

with open("arp_alive_list.txt", "w") as file:
    for host in hosts:
        file.write(host + "\n")
