#!/bin/bash

echo '#                         (1%)\r'
nmap -p- --min-rate 10000 $1 | grep "open" | cut -d "/" -f 1 | tr '\n' ',' > /tmp/anmap.txt
echo '#####                     (30%)\r'
sleep 1
echo '########                  (60%)\r'
echo "Press any key for update."
nmap -p $(cat /tmp/anmap.txt) -sV -sC --min-rate 10000 $1
echo '#######################   (100%)\r'
echo '\n'

