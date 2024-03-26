from scapy.all import *

# list of all ports to be scanned
ports = [25,80,53,443,445,8080,8443]

# function to scan port using SYN packets
def SynScan(host):

    # ans and unans are two variables for answered and unanswered responses. Flag is set to SYN.
    ans,unans = sr(IP(dst=host)/TCP(dport=ports,flags="S"),timeout=2,verbose=0)
    print("Open ports at %s:" % host)

    # s is variable for source and r for response.
    for (s,r) in ans:

        # if destination port of sent packet is equal to port from which response is coming then that port is open.
        if s[TCP].dport == r[TCP].sport:
            print(s[TCP].dport)

def DNSScan(host):
    ans,unans = sr(IP(dst=host)/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="google.com")),timeout=2,verbose=0)
    if ans:
        print("DNS Server at %s"%host)
    
host = "8.8.8.8"

SynScan(host)
DNSScan(host)
