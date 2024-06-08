import scapy.all as scapy
from scapy.layers import http
import optparse

def get_interface():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Network Interface to sniff packets")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify the interface, use --help for more information")
    
    return options.interface


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packets, filter="http")

def process_sniffed_packets(packet):
    print(packet)

interface = get_interface()
sniff(interface)