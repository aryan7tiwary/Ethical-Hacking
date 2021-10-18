#!/bin/bash

echo '#                         (1%)'
nmap -p- --min-rate 5500 $1 | grep open | cut -d "/" -f 1 | tr "\n" "," | sed 's/.$//' > /tmp/anmap.txt
echo '#####                     (15%)'
sleep 1
echo '########                  (25%)'

echo 'What type of scan do you want?'
echo "[1] Through Scan."
echo "[2] Fast Scan."

echo "Enter 1 or 2"
read VAR

echo '########                  (50%)'
echo "[*] Press any key for update."

if [[ $VAR -eq 1 ]]
then
	nmap -p $(cat /tmp/anmap.txt) -sV -sC --script=http-enum,vuln,default --min-rate 10000 $1 -oN $1_anmap.txt
fi


if [[ $VAR -eq 2 ]]
then
	echo "Press any key for update."
	nmap -p $(cat /tmp/anmap.txt) -A --min-rate 10000 $1 -oN $1_anmap.txt 
fi

cat $1_anmap.txt | xclip -selection clipboard

echo '#######################   (100%)'
echo "[*] Result has been copied to your clipboard."
