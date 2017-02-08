#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: KevinMidboe
# @Date:   2017-01-28 23:21:22
# @Last Modified by:   KevinMidboe
# @Last Modified time: 2017-02-06 11:58:31

from os import system
import xml.etree.ElementTree as ET

import sys

from time import time

def getLibraryXML():
	# Every call saves the info of session.xml to a file named plexPlaying
	system('curl --silent http://10.0.0.41:32400/library/sections/1/all > xmlMovieLib.xml')
	# XML parsing, creates a tree and saves the root node as root
	try:
		parser = ET.parse('xmlMovieLib.xml')
		xmlTreeRoot = parser.getroot()
		return xmlTreeRoot

	except xml.etree.ElementTree.ParseError:
		return None

def getMovieExistance():
	pass

def getSpecificMovieInfo(movieTitle, movieYear=None):
	xmlTreeRoot = getLibraryXML()

	try:
		treeSize = int(xmlTreeRoot.get('size'))
	except TypeError:
		return None


	if (treeSize > 0):
		for video in xmlTreeRoot.findall('Video'):
			if video.get('title') == movieTitle:
				title = movieTitle
				year = video.get('year')
				if movieYear == None or movieYear == year:
					mediaInfo = video.find('Media')
					bitrate = mediaInfo.get('bitrate')
					width = mediaInfo.get('width')
					height = mediaInfo.get('height')

					return { 'title':title, 'year': year, 'bitrate':bitrate, 
						'width':width, 'height':height }
				else:
					# field: 404?
					return { 'Error': 'Movie matching that year does not exist, did '\
						'you mean ' + title + ' (' + year + ')?'}
		
		# Return none

def plexMovies(xmlTreeRoot, query='title'):
	test = int(xmlTreeRoot.get('size'))
	sys.exit()
	# The root node named MediaContainer has a size variable that holds number of active processes.
	# If this is '0' then there are none playing, no need to compute.
	if (root.get('size') != '0'):
		# Goes through all the 'video' elements in MediaContainer
		for video in root.findall('Video'):
			if query=='title' or query=='year':
				result = video.get(query)
				print(result)

			elif query=='bitrate' or query=='width' or query=='height':
				mediaInfo = video.find('Media')
				result = mediaInfo.get(query)
				print(result)

if __name__ == '__main__':
	# Query: !title, !year, bitrate, width, height
	start_time = time()
	# xmlTreeRoot = getLibraryXML()
	# plexMovies(xmlTreeRoot)

	print(getSpecificMovieInfo('10 Cloverfield Lane'))
	print("--- %s seconds ---" % (time() - start_time))