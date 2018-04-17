import Crypto
import M2Crypto
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
from base64 import b64decode

from scapy.all import *
topo = ["S1","S2","S3"]
def test(packet):
    import Crypto
    from Crypto.Signature import PKCS1_v1_5
    from Crypto.Hash import SHA256 
    data = (packet[UDP].payload) 
    key1 = RSA.importKey(open("pub_key_switch1.pem").read())
    key2 = RSA.importKey(open("pub_key_switch2.pem").read())
    key3 = RSA.importKey(open("pub_key_switch3.pem").read())
    digest1=SHA256.new()
    digest2=SHA256.new()
    digest3=SHA256.new()
    digest1.update("S1")
    digest2.update("S2")
    digest3.update("S3")
    verifier1=PKCS1_v1_5.new(key1) 
    verifier2=PKCS1_v1_5.new(key2)
    verifier3=PKCS1_v1_5.new(key3)
    if verifier1.verify(digest1, str(data)):
       print '-----CE PAQUET A PASSE PAR ***S1***-----'
    elif verifier2.verify(digest2, str(data)):
         print '-----CE PAQUET A PASSE PAR ***S2***-----'
    elif verifier3.verify(digest3, str(data)):
         print '-----CE PAQUET A PASSE PAR ***S3***-----'
    else :
         print '-----CE PAQUET NE EST PAS SECURISE-----'
def main():
    sniff(filter="udp", prn=test, store=0)
if __name__=='__main__':
   main()

