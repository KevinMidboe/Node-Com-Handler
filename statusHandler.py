#!/usr/bin/python

# March 6, 2016 	Kevin Midboe 	Utleirvegen Trondheim
# Python program that uses UDP to get and return info of server

# TODO 
# Have everything sent as JSON objects.
# Threading for multiple accesses
# Only have valid inputs, guess if slightly off.

import os
from commands import getstatusoutput
import xml.etree.ElementTree as ET

from unicodedata import normalize
from subprocess import *
from socket import *

from v1/uptime.py import timeSinceBoot

# Define the socket communicating will transfered
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))

# TODO error handling
# Function to get the temp of the cpu by getting ouput of unix command
def temp():
	p = getstatusoutput("sensors -u | awk 'Core 0 {print $2} ' | sed -n 4p")[1]
	return str(p[:p.index('.')])

# Function that returns uptime time by getting unix command output
def uptime():
	p = getstatusoutput("uptime")[1]
	return str(p)

# Get's info from session XML file by plex
def plex():
	# Every call saves the info of session.xml to a file named plexPlaying
	os.system('curl --silent 10.0.0.41:32400/status/sessions > ~/plexPy/plexPlaying.xml')

	# XML parsing, creates a tree and saves the root node as root
	tree = ET.parse('plexPy/plexPlaying.xml')
	root = tree.getroot()

	# The root node named MediaContainer has a size variable that holds number of active processes.
	# If this is '0' then there are none playing, no need to compute.
	if (root.get('size') != '0'):

		# Get load of CPU and I/O
		return_text = '\n\t' + str(os.popen('cat /proc/loadavg').read())
		return_text += '\tCur: \t' + str(root.get('size')) + '\n'

		# Goes through all the 'video' elements in MediaContainer
		for video in root.findall('Video'):
			if (video.get('type') == 'movie'):
				name = video.get('title')
				return_text += '\n\tTitle: \t' + name

			elif (video.get('type') == 'episode'):
				parentName = video.get('grandparentTitle')
				name = video.get('title')
				return_text += '\n\tTitle: \t' + name + \
					'\n\tSeries: ' + parentName

			progress = "{0:0.1f}".format(float(video.find('TranscodeSession').get('progress')))
			state = video.find('Player').get('state')
			player = video.find('Player').get('platform')
			user = video.find('User').get('title')

			return_text += str('\n\tProg : \t' + str(progress) + '\n\tPlayer: ' + player + \
				'\n\tState: \t' + state + '\n\tUser: \t' + user + '\n')

		try:
			return normalize('NFKD', return_text).encode('ascii', 'ignore')
		except TypeError:
			return return_text
	else: 
		return 'Null playing'


def i2c_plex():
	os.system('curl --silent 10.0.0.41:32400/status/sessions > ~/plexPy/plexPlaying.xml')

	# XML parsing, creates a tree and saves the root node as root
	tree = ET.parse('plexPy/plexPlaying.xml')
	root = tree.getroot()

	# The root node named MediaContainer has a size variable that holds number of active processes.
	# If this is '0' then there are none playing, no need to compute.
	if (root.get('size') != '0'):
		# Get load of CPU and I/O
		return_text = str('$Playing: ' + str(root.get('size')))

		# Goes through all the 'video' elements in MediaContainer
		for video in root.findall('Video'):
			if (video.get('type') == 'movie'):
				name = video.get('title') # Movie name

			elif (video.get('type') == 'episode'):
				name = video.get('grandparentTitle') # Series name

			user = video.find('User').get('title')

			return_text += str('$' + user[:5] + ': ' + name).encode('utf8', 'ignore')

		try:
			return normalize('NFKD', return_text).encode('utf8', 'ignore')
		except TypeError:
			return return_text
	else: 
		return '$Null playing'

# TODO more logic in formatting the return string
# Similar function as above, but formates the return string to better fit on I2C display
def i2c_uptime():
	p = getstatusoutput("uptime") # Get's the output of unix command 'uptime'
	upOutput = p[1] # Saves the ending part of stirng to variable

	# Under the handling and formatting of the output is put together and saved to string upOutput
	try:
		upOutput = upOutput[upOutput.index('up') + 2:upOutput.index('days') + 4]
	except ValueError:
		try:
			upOutput = upOutput[upOutput.index('up') + 2:upOutput.index('min') + 3]
		except ValueError:
			upOutput = upOutput[upOutput.index('up') + 3:upOutput.index(',')]

	if (len(upOutput) > 5):
		return upOutput
	else:
		return ' ' + str(upOutput)

# TODO don't rely on nums, but logicaly pick out needed info
# This function is costumized for I2C display and formates the output of unix command
# 'uptime' to get the load of first and third value of the load
def i2c_load():
	p = getstatusoutput("uptime")
	upOutput = p[1]
	loadIndex = upOutput.index('load average: ') + 14
	upOutput = upOutput[loadIndex:loadIndex + 2] + upOutput[loadIndex + 8:]
	return upOutput.replace(', ', ' ')

def get_space(text):
	try: 
		text = text.split()
		key_index = text.index('space')
		dirName = '/media/' + text[key_index + 1]
		st = os.statvfs(dirName)

		disk_free = st.f_frsize * st.f_bavail
		disk_total = st.f_frsize * st.f_blocks

		space_output = space_format(disk_free)
		space_output += '/' + space_format(disk_total)

	except OSError:
		space_output = dirName + ' is not a valid dir'

	return space_output

def space_format(size):
	if len(str(size)) > 12:
		formated = float(size) / (1024)**4
		formated = "{0:0.1f}".format(formated) + 'T'
	else:
		formated = float(size) / (1024)**3
		formated = "{0:0.0f}".format(formated) + 'G'

	return formated

def pirate(message):
	# TODO handle output from call, and better magnet parse
	magnet = message.replace('pirate ', '')
	print(magnet)
	raw = call(['transmission-remote', '-a', magnet])
	return 'Added magnet'

# This is a repeting loop that runs everytime a message is recv in socket
while True:
	# Save the message and return address to variables.
	message, address = serverSocket.recvfrom(1024)

	print(message, address) # Debug print

	# This should prob be cases and not if's, but works to get the right info user requests.
	if (message == 'temp'):
		return_message = temp()
	elif (message == 'up'):
		return_message = timeSinceBoot()
	elif (message == 'plex'):
		return_message = plex()
	elif (message.find('space') != -1):
		return_message = get_space(message)
	elif (message == 'i2c'):
		return_message = 'Uptime: ' + i2c_uptime() + '$' + \
			'Load:    ' + i2c_load() + '$' + \
			'Temp:    ' + temp() + ' celcius$' + \
			'Space:   ' + get_space('space hdd1')
		return_message += i2c_plex()
	elif (message == 'i2c_plex'):
		return_message = i2c_plex()
	elif (message == '--help'):
		return_message = 'temp\nup\nspace {option}\n'
	elif ('pirate' in message):
		return_message = pirate(message)
	else:
		return_message = 'none'

	# Returns message to return address.
	serverSocket.sendto(return_message, address)
 

