#!/usr/bin/python3

#
#Developed by Walther Galan
#
#This software is licensed under GPL 
#
#https://github.com/walthergv/hashCrack


import hashlib
import sys
from termcolor import colored

def hash_match(hash_to_match, words):
    hash_types = {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha224": hashlib.sha224,
        "sha256": hashlib.sha256,
        "sha384": hashlib.sha384,
        "sha512": hashlib.sha512,
        "sha3_224": hashlib.sha3_224,
        "sha3_256": hashlib.sha3_256,
        "sha3_384": hashlib.sha3_384,
        "sha3_512": hashlib.sha3_512,
        "blake2b": hashlib.blake2b,
        "blake2s": hashlib.blake2s
    }
    for hash_type, hash_function in hash_types.items():
        for word in words:
            encoded = hash_function(word.encode()).hexdigest()
            if encoded == hash_to_match:
                return (hash_type, word)

    return None

if len(sys.argv) != 3:
    print(colored("\nUsage: python3 hashCrack.py [hash] [dictionary]", "red"))
    sys.exit()

hash_to_match = sys.argv[1]
word_list_file = sys.argv[2]

print(""" _   _    _    ____  _   _  ____ ____      _    ____ _  __
| | | |  / \  / ___|| | | |/ ___|  _ \    / \  / ___| |/ /
| |_| | / _ \ \___ \| |_| | |   | |_) |  / _ \| |   | ' / 
|  _  |/ ___ \ ___) |  _  | |___|  _ <  / ___ \ |___| . \ 
|_| |_/_/   \_\____/|_| |_|\____|_| \_\/_/   \_\____|_|\_\"""")

with open(word_list_file, "r") as f:
    words = f.readlines()
words = [word.strip() for word in words]

result = hash_match(hash_to_match, words)

if result:
    hash_type, password = result

    print("\n" + colored("[-] HASH Cracked!", "green"))
    print("\n" + colored("[+] Hash Type: ", "blue") + colored(hash_type, "red"))
    print(colored("[+] HASH:      ", "blue") + colored(hash_to_match, "green"))
    print(colored("[+] Password:  ", "blue") + colored(password, "green") + "\n")
else:
    print(colored(f"\n[!] No match found for: {hash_to_match}", "red"))
    print(colored("[!] Try another dictionary !!\n", "red"))