#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import psutil
from platform import system

def getCpuTemp():
	# Check if sensors_temperatures exists
	if system() != 'Linux':
		return {"Error": "Temp reader is not supported for this OS."}
	# Define cpu as function of sensors_temperatures
	cpu = psutil.sensors_temperatures()

	# Array for temps for each core.
	curCpuTemps = []
	# Itterate through all cores of coretemps 
	for temp in cpu['coretemp']:
		curCpuTemps.append(temp[1]) # Append to list
		print(temp[0]+': '+str(temp[1])) # Print output
	
	# Compute avg of curCpuTemps
	avgCpuTemps = sum(curCpuTemps)/len(curCpuTemps)
	return {"CPU Temp": avgCpuTemps}


if __name__ == "__main__":
	print(getCpuTemp())