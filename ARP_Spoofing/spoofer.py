import scapy.all as scapy

target_ip = ""
target_mac = ""
router_ip = ""

packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=router_ip)
#print(scapy.ls(scapy.ARP())) # op = 1 -> ARP request, op = 2 -> ARP response
