#!/usr/bin/python3

import hashlib
import sys
import argparse
import os

arg_parser = argparse.ArgumentParser(description="Find password from MD5 hash with known salt")
arg_parser.add_argument('-w', dest='wordlist', action='store', help='specify a wordlist (must be an existing file)', required=True)
arg_parser.add_argument('-s', dest='salt', action='store', help='specify known salt', required=True)
arg_parser.add_argument('--hash', dest='hash', action='store', help='specify known hash', required=True)

args = arg_parser.parse_args()

if not os.path.exists(args.wordlist):
    arg_parser.print_help()

wordlist = open(args.wordlist, "r")
for line in wordlist:
    testing_pass = str(args.salt) + line.replace("\n", "")
    testing_hash = hashlib.md5(testing_pass.encode("utf-8")).hexdigest()
    print( '[*] Try: {}'.format(line) )

    if  args.hash == testing_hash:
        print( '[+] Password found: {}'.format(line) )
        break

wordlist.close()
 

