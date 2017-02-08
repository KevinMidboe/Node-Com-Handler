#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: KevinMidboe
# @Date:   2016-11-22 12:07:08
# @Last Modified by:   KevinMidboe
# @Last Modified time: 2016-11-28 08:14:35

import geoip2.database
import ipaddress, os

class ipLookup(object):
	"""docstring for ipLookup"""
	def __init__(self, address):
		super(ipLookup, self).__init__()
		self.databaseLocation = 'GeoLiteDatabases/city.mmdb'
		self.address = ipaddress.ip_address(address)
		self.version = self.address.version
		self.getLocation()

	def getLocation(self):
		reader = geoip2.database.Reader(self.databaseLocation)
		response = reader.city(self.address)
		self.country = response.country.name
		self.city = response.city.name
		self.region = response.subdivisions.most_specific.name
		self.postcode = response.postal.code

	def changeDatabase(self, database):
		newDatabaseLocation = 'GeoLiteDatabases/'+database+'.mmdb'
		if os.path.isfile(newDatabaseLocation):
			self.databaseLocation = newDatabaseLocation
		else:
			raise NameError('File '+newDatabaseLocation+' does not exist')

	def getDatabaseLocation(self):
		return self.databaseLocation

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)