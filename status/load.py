#!/usr/bin/env python3
from subprocess import check_output
from re import findall

def load():
  arpOutput = check_output("sudo arp-scan -l", shell=True)
  print(findall('[0-9]{1,2}[\.][0-9]{2}'))

if __name__ == '__main__':
	load()