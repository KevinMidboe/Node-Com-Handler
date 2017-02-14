#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: KevinMidboe
# @Date:   2017-01-28 10:54:06
# @Last Modified by:   KevinMidboe
# @Last Modified time: 2017-02-14 10:01:47

# f_avail = free blocks avail to non sudo
# frsize = fundamental file sys byte size
# f_blocks = total number of blocks in the filesystem

from os import statvfs
from re import sub

def sizeof(num, suffix='B'):
	for unit in ['','K','M','G','T','P','E','Z']:
		if abs(num) < 1024.0:
			return "%3.1f%s%s" % (num, unit, suffix)
		num /= 1024.0
	return "%.1f%s%s" % (num, 'Y', suffix)

# diskUsage uses statvfs to calculate disk size and availability for given disk
def diskUsage(optionalPath=None):
	path = '/'
	if optionalPath != None:
		path += sub('\+', '/', optionalPath)

	try:
		s = statvfs(path)
		byteLeft = s.f_bavail * s.f_frsize
		byteTotal = s.f_blocks * s.f_frsize
		byteUsed = byteTotal-byteLeft

		return { 'left':sizeof(byteLeft), 'used':sizeof(byteUsed), 'total':sizeof(byteTotal) }

	except FileNotFoundError:
		return None
	except TypeError:
		return None

if __name__=="__main__":
	n = diskUsage('/')
	print(n)
