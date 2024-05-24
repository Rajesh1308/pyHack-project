#!bin/bash

#######################################################################
# Creator : Rajesh A                                                  #
# Date : 24-05-2024                                                   #
# This script installs the necessory tools sets up the container      #
# as a hacking machine to run MITM. Atfer installation, it runs the   # 
# network scanner                                                     #
#######################################################################


apt install python-is-python3 python3-pip iputils-ping net-tools -y
apt install git -y
pip install -r requirements.txt
git clone https://github.com/Rajesh1308/pyHack-project.git
cd pyHack-project/Network_scanner/
echo "Enter the target ip/range : "
read ip
python scanner.py -t $ip