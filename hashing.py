#!/usr/bin/python

import hashlib
import sys
import os
import platform

sys.stdout.write("\x1b[8;24;90t")

### OPEN-SOURCE CODE LICENSES ###
# # Visual Progress Bar License# #
# The MIT License (MIT)
# Copyright (c) 2016 Vladimir Ignatev
#
# Permission is hereby granted, free of charge, to any person obtaining 
# a copy of this software and associated documentation files (the "Software"), 
# to deal in the Software without restriction, including without limitation 
# the rights to use, copy, modify, merge, publish, distribute, sublicense, 
# and/or sell copies of the Software, and to permit persons to whom the Software 
# is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included 
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
# FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT
# OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# # END OF PROGRESS BAR LICENSE # #
### END OF LICENSES ###

if platform.system() == "Windows":
	clear = lambda: os.system('cls')
else:
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

def exitHelp():
	print("Usage: [option] (filename)")
	print(" -<option>:")
	print("  -c - Check file integrity by comparing with existing hash file(Requires filename after)")
	print("  -g - Generate a hash file to check file integrity later(Requires filename after)")
	print("  -h - Show this help page")
	print("")
	print(" *()* Required for some options")
	sys.exit()

def progress(count, total, status=''):
  bar_len = 60
  filled_len = int(round(bar_len * count / float(total)))
  percents = round(100.0 * count / float(total), 1)
  bar = '=' * filled_len + '-' * (bar_len - filled_len)
  sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
  sys.stdout.flush()
	#For license check above

#Introduction
clear()
print(BOLD("Integrity check v.0.2 By Logsys"))
print("\nLicensed under MIT License.\nFor more information check https://github.com/logsys11/Integrity-Check-Script\n\n")
#print(str(ARGLIST))
for i in range(0,len(ARGLIST)):
	if ARGLIST[i] == "-h":
		exitHelp()
	elif ARGLIST[i] == "-c":
		filename = ARGLIST[i+1]
		break
	elif ARGLIST[i] == "-g":
		GENERATE = True
		filename = ARGLIST[i+1]
		break
	else:
		if i == len(ARGLIST):
			exitHelp()	

md5hasher = hashlib.md5()
sha1hasher = hashlib.sha1()
sha256 = hashlib.sha256()

with open(filename, 'rb') as afile:
	print("Loading file " + filename)
	totalbuf = BLOCKSIZE
	totalsize = os.fstat(afile.fileno()).st_size
	print("File size is: " + str(round(totalsize/1024,1)) + "KB\n")
	buf = afile.read(BLOCKSIZE)
	
	while len(buf) > 0:
		md5hasher.update(buf)
		sha1hasher.update(buf)
		sha256.update(buf)
		totalbuf = totalbuf + BLOCKSIZE
		if totalbuf > totalsize:
			totalbuf = totalsize
		progress(totalbuf,totalsize,status=' Reading file...')
		buf = afile.read(BLOCKSIZE)
		
sys.stdout.write('\n\n')
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
