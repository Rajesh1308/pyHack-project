#!/usr/bin/env python

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New mac address to be changed")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify the interface, use --help for more information")
    if not options.new_mac:
        parser.error("[-] Please specify the MAC address, use --help for more information")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " t0 " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

    subprocess.check_output(["ifconfig", interface])


options = get_arguments()
change_mac(options.interface, options.new_mac)
