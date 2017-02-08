#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: KevinMidboe
# @Date:   2016-11-22 12:18:17
# @Last Modified by:   KevinMidboe
# @Last Modified time: 2016-12-01 20:12:48

import ipLookup

if __name__ == '__main__':
	ipList = {}
	ip = '91.22.128.66'
	ip = '85.164.178.87'
	if ip not in ipList:
		ipList.update({ip:ipLookup.ipLookup(ip)})

	address = ipList[ip]
	print(address)
