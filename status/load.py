#!/usr/bin/env python3
from subprocess import check_output
from re import findall
from platform import system

def load():
	sysName = system()
	if sysName == 'Linux':
		arpOutput = check_output("cat /proc/loadavg", shell=True)
		arpOutput = arpOutput.decode()
		return findall('[0-9]{1,2}[\.][0-9]{2}', arpOutput)
	elif sysName == 'Darwin':
		arpOutput = check_output("uptime", shell=True)
		arpOutput = arpOutput.decode()
		return findall('[0-9]{1,2}[\.][0-9]{2}', arpOutput)

	return {"Error": "Running OS does not supported load."}

if __name__ == '__main__':
	print(load())
