import dns
import dns.resolver
import socket

# There is a chance that a single IP address is hosting multiple subdomains. Therefore trying to get hostname using address
def ReverseDNS(ip):
    try:
        result = socket.gethostbyaddr(ip)
        return [result[0]]+result[1]
    except socket.herror:
        return None

def DNSRequest(domain):
    ips = []
    try:
        
        # using DNS' resolver module for A record and check if the domain exists
        result = dns.resolver.resolve(domain,'A')

        # if DNS resolves and gets assigned to variable "result"
        if result:  
            print(domain)
            for answer in result:
                print(answer)
                print("Domain Names: %s" %ReverseDNS(str(answer)))
    except (dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return []
    return ips

# Function to join third level domain with domain name
def SubdomainSearch(domain, dictionary,nums):
    successes = []
    for word in dictionary:
        subdomain = word+"."+domain
        DNSRequest(subdomain)

        # if nums is True it will add numbers (0-9) as suffix to every third level domain, e.g. www2.google.com
        if nums:
            for i in range(0,10):
                s = word+str(i)+"."+domain
                DNSRequest(s)

domain = "google.com"
d = "subdomains.txt"
dictionary = []
with open(d,"r") as f:
    dictionary = f.read().splitlines()
SubdomainSearch(domain,dictionary,True)