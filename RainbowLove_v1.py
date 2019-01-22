#!/usr/local/bin/python3

"""
      AUTHOR: Jerry Kim Gomez
      SCRIPT: Rainbow Love
      VERSION: Version 1
      DATE: June 14, 2018

      DESC: This script will ask a user for a plain text file of 
      passwords, encrypt the passwords, and finally append the 
      encrypted password and the password into a Rainbow Table.
"""

from datetime import datetime

import hashlib	# Encryption module for the "hashlib" library.
import time		# For time stamping output with "time.ctime()".
import sys
import os


# This function reads a file of passwords, encrypts the passwords into
# MD5 hashes, and then appends the hash and the password into the file
# RainbowTable.txt
def theHasher(fileManage):
	appendHash = open('RainbowTable.txt', 'a')
	appendHash.write("\n\nScript started at: " + time.ctime() + "\n\n")
	for i in fileManage:
		hashed256 = hashlib.sha256(i.encode()).hexdigest()
		hashed256strip = hashlib.sha256(i.rstrip().encode()).hexdigest()
		hashed512 = hashlib.sha512(i.encode()).hexdigest()
		hashed512strip = hashlib.sha512(i.rstrip().encode()).hexdigest()
		appendHash.write(hashed256 + ':' + hashed256strip + ':' + hashed512 + ':' + hashed512strip + ":" + i)

	appendHash.write("\n\nScripted ended at: " + time.ctime() + "\n\n")
	appendHash.close()
	

# The main fuction asks the user for a list of passwords for the
# script to encrypt and add to a Rainbow Table.
def main():
	fileInput = input ("Enter a file name: ")
	fileManage = open(fileInput)

	theHasher(fileManage)
	fileManage.close()


if __name__ == "__main__":
	main()




