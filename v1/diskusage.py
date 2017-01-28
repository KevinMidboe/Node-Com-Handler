#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: KevinMidboe
# @Date:   2017-01-28 10:54:06
# @Last Modified by:   KevinMidboe
# @Last Modified time: 2017-01-28 13:23:07

from os import statvfs
	
def sizeof(num, suffix='B'):
	for unit in ['','K','M','G','T','P','E','Z']:
		if abs(num) < 1000.0:
			return "%3.1f%s%s" % (num, unit, suffix)
		num /= 1000.0
	return "%.1f%s%s" % (num, 'Y', suffix)

def diskUsage(path='/'):
	s = statvfs(path)
	byteLeft = s.f_bavail * s.f_frsize
	byteTotal = s.f_blocks * s.f_frsize
	byteUsed = byteTotal-byteLeft

	return { 'left':sizeof(byteLeft), 'used':sizeof(byteUsed), 'total':sizeof(byteTotal) }

if __name__=="__main__":
	n = diskUsage('/')
	print(n)