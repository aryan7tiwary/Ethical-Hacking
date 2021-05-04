#!/bin/python3

#modules
import sys
import socket
from datetime import datetime


#interaction
print("""____             __     _____
   / __ \____  _____/ /_   / ___/_________ _____  ____  ___  _____
  / /_/ / __ \/ ___/ __/   \__ \/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
 / ____/ /_/ / /  / /_    ___/ / /__/ /_/ / / / / / / /  __/ /
/_/    \____/_/   \__/   /____/\___/\__,_/_/ /_/_/ /_/\___/_/ """)      

                                       
#target IP
if len(sys.argv) == 2:
  #hostname to IPv4
  target = socket.gethostbyname(sys.argv[1])

else:
  print("Wrong syntax.")
  print("Syntax: python3 scanner_v1.0.py <ip>")
  sys.exit()

#interaction
print("*" * 50)
print("Scanning target: "+target)
#Time when process started
print("Time started: "+str(datetime.now()))
print("*" * 50)

#input for range of port
a = int(input("Enter from range: "))
b = int(input("Enter to range: "))
try:
  for port in range(a,b):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #time spent on each port
    socket.setdefaulttimeout(1) #time is float type
    result= s.connect_ex((target,port))
    print("Checking port {}".format(port))

    #output will be 0 if connection is established
    if result == 0:
      print("Port {} is open".format(port))
      s.close()

#output incase of errors
except KeyboardInterrupt:
  print("\nExiting program.")
  sys.exit()

except socket.gaierror:
  print("Hostname could not be resolved.")

except socket.error:
  print("Unable to establish connection with the server")
  sys.exit
