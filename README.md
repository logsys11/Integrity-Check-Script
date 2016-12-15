# Integrity-Check-Script
## Introduction
  This simple script began as a project to try and improve my programming skills, as I am still **NOT** in any University, however would love to participate in a competition between schools and, again, needed to improve my programming skills.
  The script is easy to run, only requires python to run, and it generates 3 hashes and outputs them into a file to check later if they are a match.
## Usage
  ./scriptname <option> <filename>
  options: 
    -g: Generates hash(for first time)
    -c: Checks file if hashes have been generated
    -h: Shows a help message
  filename is required after -g or -c
  use ./ only if you are in a Linux or Mac OS X environment
## What happens inside
  A new file is generated with the same name of your file, adding only a new extension .hash, containing an MD5 hash, SHA1 hash and SHA256 hash inside.
## First Run
  It's recommended that you check the script's integrity by running itself on the script(download .hash file alongside the script)
  (./scriptname -c scriptname).\n
  If you are on Linux or Mac OS X(not sure about the last one), run chmod +x scriptname before using it.
## Licensing
  This script is licensed under a MIT license. Check the file LICENSE in this repository
## Changelog
  v0.2 - Changed GUI, added new smaller features, improved performance slightly.
  v0.1 - First launched script
