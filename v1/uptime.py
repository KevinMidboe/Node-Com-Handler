#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: KevinMidboe
# @Date:   2017-01-27 19:48:42
# @Last Modified by:   KevinMidboe
# @Last Modified time: 2017-01-31 23:13:20

# TODO add better error handling to return statements

from psutil import boot_time
from time import time

def secToDay(seconds):
	days = int(seconds/86400)
	if days is 1:
		return str(days)+' day'
	else:
		return str(days)+' days'

def secToHour(seconds):
	hours = (seconds)//3600
	minutes = (seconds - hours*3600)//60
	hourMinutes = '%02d' % hours +':'+ '%02d' % minutes
	return hourMinutes

def timeSinceBoot():
	bootTime = boot_time()	# Use psutil 'boot_time' to get seconds since start
	currTime = time() 	# Use 'time()' to get seconds currently
	deltaSeconds = int(currTime-bootTime) 

	# Return in day format
	if deltaSeconds >= 86400:
		return secToDay(deltaSeconds)

	# Return in hour format
	elif deltaSeconds < 86400 and deltaSeconds >= 0:
		return secToHour(deltaSeconds)
	else:
		# TODO Throw error
		return None

if __name__=="__main__":
	print(timeSinceBoot())