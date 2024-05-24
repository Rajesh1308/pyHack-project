## Play with networks - pyHack-project
pyHack-project is a collection of programs that could perform network related attacks like ARP spoofing, Network scanning, DNS spoofing, etc.
This project was developed and tested in containerized environment. It is adviced to run the program in ubuntu docker container and per the instructions.
If you want to test it in real time, connect the container to a bridge network.

<h2>Instruction</h2>
Install docker in the system and run the ubuntu container using the following command<br>
<table><tr>
    <th>docker run -it --name attack-machine ubuntu</th>
</tr></table>
It installs the ubuntu image and runs it with the name 'attack-machine' (You can choose any other name). 
It opens the bash terminal for the machine. If not, verify whether the conainer is up and running using the command:
<table><tr>
    <th>docker ps</th>
</tr></table>
And then run,
<table><tr>
    <th>docker exec -it <conatiner-name></th>
</tr></table>
<br>
Once you enter the terminal, update the packages and install nano (or vim) text editor. Then open the text editor,
<table><tr>
    <th>apt update && apt-get install nano</th>
</tr></table>
 Then open the text editor,
 <table><tr>
    <th>nano setup-attacker.sh</th>
</tr></table>
Copy and paste the content of the setup-attacker.sh file into the local file and save it. Provide the executable permission and run the script.
<br>
It installs the required tools like `python3, pip, iputils, net-tools and scapy` and runs the network scanner. 
<br>
You need to provide the ip address/range to be scanned. 
Now you can play with the scripts.
Navigate to the project folder and run the programs.
