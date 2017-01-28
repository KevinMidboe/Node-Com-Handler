#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: KevinMidboe
# @Date:   2017-01-27 19:48:42
# @Last Modified by:   KevinMidboe
# @Last Modified time: 2017-01-28 13:30:19

from psutil import boot_time
from time import time

def timeSinceBoot():
	# Use psutil 'boot_time' to get seconds since start
	bootTime = boot_time()
	# Use 'time()' to get seconds currently
	currTime = time()
	delta = int(currTime-bootTime) 

	# Return in day format
	if delta >= 86400:
		# TODO error handling
		rt = int(delta/86400)
		if rt is 1:
			return str(rt)+' day'
		else:
			return str(rt)+' days'

	# Return in hour format
	elif delta < 86400 and delta >= 0:
		# TODO error handling
		hours = (delta)//3600
		minutes = (delta - hours*3600)//60
		rt = '%02d' % hours +':'+ '%02d' % minutes
		return rt
	else:
		# Throw error
		return 'Null'

if __name__=="__main__":
	print(timeSinceBoot())