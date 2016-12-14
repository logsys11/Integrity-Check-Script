import hashlib
import sys
import os

clear = lambda: os.system('clear')

BLOCKSIZE = 65536
ARGLIST = sys.argv
GENERATE = False
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def BOLD(string):
	return bcolors.BOLD + string + bcolors.ENDC
	
def OKGREEN(string):
	return bcolors.OKGREEN + string + bcolors.ENDC

def FAIL(string):
	return bcolors.FAIL + string + bcolors.ENDC

def WARNING(string):
	return bcolors.WARNING + string + bcolors.ENDC

def UNDERLINE(string):
	return bcolors.UNDERLINE + string + bcolors.ENDC

#Introduction
clear()
print(BOLD("Integrity check v.0.1 By Logsys"))
print("")
print("All rights reserved. Copyright 2016\n")
if len(ARGLIST) > 1:
	if (ARGLIST[1] == "check"):
		filename = ARGLIST[2]
	elif (ARGLIST[1] == "generate"):
		filename = ARGLIST[2]
		GENERATE = True
	else:
		print(" Usage: <flag> <filename>")
		print("   -<flag>:")
		print("     check - Check file integrity by comparing with existing hash file")
		print("     generate - Generate a hash file to check file integrity later")
else:
	print("   Usage: <flag> <filename>")
	print("-<flag>:")
	print("  check - Check file integrity by comparing with existing hash file")
	print("  generate - Generate a hash file to check file integrity later")
	sys.exit()
	

md5hasher = hashlib.md5()
sha1hasher = hashlib.sha1()
sha256 = hashlib.sha256()

with open(filename, 'rb') as afile:
	buf = afile.read(BLOCKSIZE)
	while len(buf) > 0:
		md5hasher.update(buf)
		sha1hasher.update(buf)
		sha256.update(buf)
		buf = afile.read(BLOCKSIZE)
		
md5hash = md5hasher.hexdigest()
sha1hash = sha1hasher.hexdigest()
_sha256 = sha256.hexdigest()

if GENERATE:
	with open(filename + '.hash', 'w') as thefile:
		thefile.write(md5hash + '\n' + sha1hash + '\n' + _sha256 + '\n' + 'Generated in a special script by logsys')
		print("MD5 hash: " + BOLD(md5hash))
		print("SHA1 hash: " + BOLD(sha1hash))
		print("SHA256 hash: " + BOLD(_sha256))
else:
	print("Current MD5 hash: " + bcolors.BOLD + md5hash + bcolors.ENDC)
	print("Current SHA-1 hash: " + bcolors.BOLD + sha1hash + bcolors.ENDC)
	print("Current SHA-256 hash: " + BOLD(_sha256))
	print("")
	with open(filename + '.hash', 'rb') as thefile:
		extMD5 = thefile.readline()
		extMD5 = extMD5.rstrip('\n')
		extSHA1 = thefile.readline()
		extSHA1 = extSHA1.rstrip('\n')
		extSHA256 = thefile.readline().rstrip('\n')
		print("Expected MD5 hash: " + bcolors.BOLD + extMD5 + bcolors.ENDC + "\nExpected SHA-1 hash: " + bcolors.BOLD + extSHA1 + bcolors.ENDC)
		print("Expected SHA256 hash: " + BOLD(extSHA256) + "\n")
		if (str(extMD5) == str(md5hash)) and (str(extSHA1) == str(sha1hash)) and (str(extSHA256) == str(_sha256)):
			print(bcolors.OKGREEN + "CHECK" + bcolors.ENDC)
		else:
			print(bcolors.FAIL + "NO MATCH!" + bcolors.ENDC)
