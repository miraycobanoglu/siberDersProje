from scapy.all import IP, ICMP, send

paket = IP(src="172.16.107.31", dst="172.16.107.32") / ICMP(type=0)
send(paket, count=1)

# Saldiri yapan IP: 172.16.107.32
# Miray Çobanoğlu