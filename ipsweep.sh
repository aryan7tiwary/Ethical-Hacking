#!/bin/bash

echo "Enter first three point of IP address. Eg: 192.168.1"
read input
echo
echo "Available IP addresses:"
for ip in {1..254};
do
	(ping -c 1 $input.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &)
done
