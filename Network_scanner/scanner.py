import scapy.all as scapy
import optparse


def get_ip():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target_ip", help="Target IP address")
    (options, arguments) = parser.parse_args()
    if not options.target_ip:
        parser.error("[-] Please specify the target IP, use --help for more information")
    
    return options.target_ip




def scan(ip):
    arp_request = scapy.ARP(pdst=ip) 
    #arp_request.pdst = ip
    #print(arp_request.summary())
    #scapy.ls(arp_request)

    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # Fame creation with dest
    #scapy.ls(scapy.Ether())
    #print(broadcast.summary())

    arp_request_broadcast = broadcast/arp_request
    #print(arp_request_broadcast.summary())
    #arp_request_broadcast.show()

    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=2, verbose=False) #send and receive packets
    #print(answered.summary())

    print("IP\t\t\t\tMAC Address\t\t")
    print("------------------------------------------")
    for elements in answered:
        print(elements[1].psrc + "\t\t\t" + elements[1].hwsrc)


ip = get_ip()

scan(ip)