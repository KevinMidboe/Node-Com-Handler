#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import psutil

def getCpuTemp():
	# Check if sensors_temperatures exists
	try:
		# Define cpu as function of sensors_temperatures
		cpu = psutil.sensors_temperatures()
	except AttributeError:
		error = "'sensors_temperatures' is not supported in this verison of psutil or your OS."
		print(error)
		return None

	# Array for temps for each core.
	curCpuTemps = []
	# Itterate through all cores of coretemps 
	for temp in cpu['coretemp']:
		curCpuTemps.append(temp[1]) # Append to list
		print(temp[0]+': '+str(temp[1])) # Print output
	
	# Check if len of curCpuTemps is something so not to 
	# calculate on a empty list
	if len(curCpuTemps) > 0:
		# Compute avg of curCpuTemps
		avgCpuTemps = sum(curCpuTemps)/len(curCpuTemps)
		return avgCpuTemps
		print("Avg: " + str(avgCpuTemps))
	else:
		print("Couldn't get cpu temp. (division by zero)")
		return None


if __name__ == "__main__":
	print(getCpuTemp())