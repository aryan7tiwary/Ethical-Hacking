#!/bin/python3


import zipfile          # zipfile is a module to work with zip format files
from tqdm import tqdm   # tqdm is a module for status bar 


# the password list path you want to use, must be available in the current directory
wordlist = "wordlist.txt"
# the zip file you want to crack its password
zip_file = "test.zip"


# initialize the Zip File object
zip_file = zipfile.ZipFile(zip_file)
# count the number of words in this wordlist
n_words = len(list(open(wordlist, "rb")))
# print the total number of passwords
print("Total passwords to test:", n_words)


with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+] Password found:", word.decode().strip())
            exit(0)
print("[!] Password not found, try other wordlist.") 
