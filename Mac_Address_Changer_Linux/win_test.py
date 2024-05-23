#!/usr/bin/env python

import subprocess
import re



def change_mac():
    print("[+] Changing MAC address " )

    output = subprocess.check_output(["ipconfig"])
    print(output)
    matches = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(output))
    print(matches)

change_mac()
