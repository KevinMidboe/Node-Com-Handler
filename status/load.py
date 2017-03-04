#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: KevinMidboe
# @Date:   2017-02-15 23:45:16
# @Last Modified by:   KevinMidboe
# @Last Modified time: 2017-02-18 11:42:42

from subprocess import check_output
from re import findall
from platform import system

def load():
	sysName = system() 	# Get system name
	if sysName == 'Linux':
		arpOutput = check_output("cat /proc/loadavg", shell=True)
	elif sysName == 'Darwin': 	# macOS
		arpOutput = check_output("uptime", shell=True)
	else:
		return {"errors": "Running OS does not supported load."}
		
	arpOutput = arpOutput.decode()
	return {"loads": findall('[0-9]{1,2}[\.][0-9]{2}', arpOutput)}

if __name__ == '__main__':
	print(load())
