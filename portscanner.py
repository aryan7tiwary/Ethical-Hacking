#!/bin/python3
import socket
import sys
import pyfiglet
from datetime import datetime

banner = pyfiglet.figlet_format("Port Scanner")
print(banner)

now = datetime.now()

target = input("Enter IP to scan:")

print("-" * 50)
print("Scanning target :"+target)
print("Time started :"+str(datetime.now()))
print("-" * 50)

a = int(input("Enter first range:"))
b = int(input("Enter second eange:"))

try:
	for port in range(a,b+1):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
	
		result = s.connect_ex((target, port))
		if result == 0:
			print("Port {} : OPEN".format(port))
		s.close()
		
except KeyboardInterrupt:
	print("\nExiting program")
	sys.exit()
	
except socket.gaierror:
	print("\nHostname could not be resolved")
	sys.exit()
	
except socket.error:
	print("\nServer not responding")
	sys.exit()	
	
print("Time taken: {}".format(datetime.now()-now))
