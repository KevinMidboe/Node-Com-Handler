#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: KevinMidboe
# @Date:   2016-11-22 16:05:18
# @Last Modified by:   KevinMidboe
# @Last Modified time: 2016-11-22 17:07:41

import subprocess, re

class uptime(object):
	"""docstring for uptime"""
	def __init__(self):
		super(uptime, self).__init__()
		raw = subprocess.Popen('uptime', stdout=subprocess.PIPE)
		output, error = raw.communicate()
		uptimeList = output.decode('utf-8').split(', ')
		
		self.duration(uptimeList[0])
		self.users(uptimeList[2])
		self.load(uptimeList[3])

	def duration(self, outputString):
		self.duration = re.sub(r'.*up ', '', outputString)

	def users(self, outputString):
		self.users = outputString

	def load(self, outputString):
		loadValues = re.sub(r'.*load averages: ', '', outputString)
		self.load = re.sub(r'\n', '', loadValues)
		self.load_minute, self.load_fiveminute, self.load_fiftenminute = self.load.split(' ')

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)