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
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packets)

def process_sniffed_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        print(scapy.ls(packet))
        http_request = packet[http.HTTPRequest]
        method = http_request.Method
        path = http_request.Path

        # Check for presence of Raw layer (may not always contain data)
        if packet.haslayer(scapy.Raw):
            request_body = packet[scapy.Raw].load.decode("utf-8", errors="ignore")  # Decode with error handling
        else:
            request_body = "(No request body)"

        print(f"HTTP Request: {method} {path}")
        print(f"Request Body:\n{request_body}")

interface = get_interface()
sniff(interface)