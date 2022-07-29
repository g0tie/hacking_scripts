#!/usr/bin/env python3

import string
import sys

def usage():
	print("Usage: generateAlphabet.py [OPTION]")
	print("\n OPTIONS: \n -U: uppercase -L: lowercase")

if len(sys.argv) > 1:

	if sys.argv[1] == "-U":
		alphabet = string.ascii_uppercase
	elif sys.argv[1] == "-L":
		alphabet = string.ascii_lowercase

	else :
		usage()
		sys.exit()

	for letter in alphabet:
		print(letter)

else :
	usage()
	sys.exit()


