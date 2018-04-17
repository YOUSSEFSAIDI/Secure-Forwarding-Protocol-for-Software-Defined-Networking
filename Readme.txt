1- Mininet Download:
we need to connect to the web page: “http://mininet.org/download/” and download the Mininet VM image. Then we need to download Virtual Box from this link “https://www.virtualbox.org/wiki/Downloads”
2- Virtual Box configuration: we need to follow the link “http://mininet.org/vm-setup-notes/”
3- After finishing the installation, we need to open the mininet machine on the virtual box  with login and password: “mininet”. Then enter the command “ifconfig” and get the ip address of the eth1
4- Open a new terminal and ssh to this address
5- Copy the python script Mytopo.py in the directory mininet/mininet
6- Create a directory under mininet/mininet for example project.
7- Create for each switch a directory mininet/mininet/project/switchi and copy the scripts(script_switchi.py) and the keys(sci-privkey.py and pub_key_switchi.py) for each switch in his folder.
8- For h5 create a direcory /mininet/mininet/project/host5 and copy the script(script_host5.py) and all the public keys ( pub_key_switchi.py)
9- Under mininet/pox run the pox controller: $ ./pox.py forwarding.l3_learning -fakeways=192.168.4.1,192.168.5.1,192.168.6.1 misc.packet_dump samples.pretty_log log.level --DEBUG
10- Open a new window and under mininet/mininet run the topology: sudo python Mytopo.py.
11- In the mininet window run the command: xterm s1 s2 s3 h5
12- For each switch window go to the right directory (mininet/mininet/project/switchi/) and run the script: python script_switchi.py
13- For the host window go to the right directory (mininet/mininet/project/host5) and run the script: python script_host5.py
14- In the mininet window run the ping from any host to host5: hi ping -c1 h5 
15- If you want to test on any other host just run the script_host5.py on that host.
