from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from base64 import b64encode, b64decode
from scapy.all import *
add = set(["192.168.4.2","192.168.5.2","192.168.5.3","192.168.6.2","192.168.6.3"])
def sniffPackets(packet):
    from Crypto.Signature import PKCS1_v1_5
    from Crypto.Hash import SHA256
    from base64 import b64encode, b64decode

    if packet.haslayer(IP) and packet[IP].src in add:
       pckt_src=packet[IP].src
       pckt_dst=packet[IP].dst
       pckt_ttl=packet[IP].ttl
       print('IP packet:%s is going to %s and has ttl value %s') % (pckt_src,pckt_dst,pckt_ttl)
       message = "S1"
       digest = SHA256.new()
       digest.update(message)
       # Read shared key from file
       private_key = RSA.importKey(open("sc1-privkey.pem").read())
       # Load private key and sign message
       signer = PKCS1_v1_5.new(private_key)
       sig = signer.sign(digest)
       packet1 = IP(dst=pckt_dst)/UDP()/ Raw(load=sig)
       send(packet1)
def main():
    print('custom packet sniffer')
    sniff(filter="icmp",prn=sniffPackets, iface='s1-eth2')
if __name__=='__main__':
   main()

