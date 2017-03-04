#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: KevinMidboe
# @Date:   2017-02-15 23:37:36
# @Last Modified by:   KevinMidboe
# @Last Modified time: 2017-02-15 23:49:18

import psutil
from platform import system

# TODO: Add cpu reading for macOS

def getCpuTemp():
	sysName = system()
	if sysName != 'Linux':
		return {"Error": "Running OS does not support cpu temp reads."}

	# Define cpu as function of sensors_temperatures
	cpu = psutil.sensors_temperatures()

	# Array for temps for each core.
	curCpuTemps = []
	# Itterate through all cores of coretemps 
	for temp in cpu['coretemp']:
		curCpuTemps.append(temp[1]) # Append to list
		print(temp[0]+': '+str(temp[1])) # Print output
	
	avgCpuTemps = sum(curCpuTemps)/len(curCpuTemps)
	return {"Avg cpu temp": avgCpuTemps, "Max cpu temp": max(curCpuTemps), 
		"Min cpu temp": min(curCpuTemps)}
	

if __name__ == "__main__":
	print(getCpuTemp())